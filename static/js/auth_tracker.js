/**
 * FoodSight AI (Local App) - Auth, Profile Wizard, Calorie Tracker & Meal Log
 * ==============================================================================
 * Uses server-side auth (/api/auth/login, /api/auth/signup) + localStorage for
 * the calorie profile and daily meal log (no backend changes required).
 */

// ─── Constants ────────────────────────────────────────────────────────────────
const FS_PROFILE_KEY = 'fsProfile';
const MEAL_ORDER = ['Breakfast', 'Lunch', 'Snack', 'Dinner'];
const MEAL_EMOJIS = { Breakfast: '🍳', Lunch: '🍛', Snack: '☕', Dinner: '🍽️' };

// ─── localStorage helpers ─────────────────────────────────────────────────────
function getTodayKey() {
    const d = new Date();
    return `fsLog_${d.getFullYear()}_${d.getMonth() + 1}_${d.getDate()}`;
}
function getTodayLog() {
    try { return JSON.parse(localStorage.getItem(getTodayKey())) || []; } catch { return []; }
}
function saveTodayLog(log) { localStorage.setItem(getTodayKey(), JSON.stringify(log)); }
function loadUserProfile() { try { return JSON.parse(localStorage.getItem(FS_PROFILE_KEY)); } catch { return null; } }
function saveUserProfile(p) { localStorage.setItem(FS_PROFILE_KEY, JSON.stringify(p)); }

// ─── BMR / TDEE (Mifflin–St Jeor) ────────────────────────────────────────────
function calculateTDEE(p) {
    const { age, gender, heightCm, weightKg, activityLevel, goalAdjust } = p;
    const bmr = gender === 'female'
        ? (10 * weightKg) + (6.25 * heightCm) - (5 * age) - 161
        : (10 * weightKg) + (6.25 * heightCm) - (5 * age) + 5;
    const tdee = Math.round(bmr * (parseFloat(activityLevel) || 1.55));
    const goal = Math.max(1200, tdee + (parseInt(goalAdjust) || 0));
    return { bmr: Math.round(bmr), tdee, goal };
}
function getCalorieGoal() {
    const p = loadUserProfile();
    return (p && p.calorieGoal) ? p.calorieGoal : 2000;
}

// ─── App flow init ────────────────────────────────────────────────────────────
async function initAppFlow() {
    try {
        const res = await fetch('/api/auth/status');
        const data = await res.json();
        if (data.authenticated) {
            hideAuthScreen();
            onLoggedIn(data.username);
        } else {
            showAuthScreen();
        }
    } catch {
        // Server unreachable – still show auth screen
        showAuthScreen();
    }
}

// ─── Auth Screen ──────────────────────────────────────────────────────────────
function showAuthScreen() {
    const el = document.getElementById('authScreen');
    if (el) { el.style.display = 'flex'; el.style.opacity = '1'; el.style.pointerEvents = 'auto'; }
}
function hideAuthScreen() {
    const el = document.getElementById('authScreen');
    if (!el) return;
    el.style.transition = 'opacity 0.4s ease';
    el.style.opacity = '0';
    el.style.pointerEvents = 'none';
    setTimeout(() => { el.style.display = 'none'; }, 420);
}

function setupAuthScreenListeners() {
    // Toggle sign-in / sign-up panels
    document.getElementById('showSignupToggle')?.addEventListener('click', e => {
        e.preventDefault();
        document.getElementById('authLoginForm').style.display = 'none';
        document.getElementById('authSignupForm').style.display = 'block';
    });
    document.getElementById('showLoginToggle')?.addEventListener('click', e => {
        e.preventDefault();
        document.getElementById('authSignupForm').style.display = 'none';
        document.getElementById('authLoginForm').style.display = 'block';
    });

    // Login via server
    document.getElementById('authLoginForm')?.addEventListener('submit', async e => {
        e.preventDefault();
        const username = document.getElementById('authLoginUsername').value.trim();
        const password = document.getElementById('authLoginPassword').value;
        const errEl = document.getElementById('authLoginError');
        try {
            const res = await fetch('/api/auth/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });
            const data = await res.json();
            if (res.ok) {
                hideAuthScreen();
                onLoggedIn(data.username || username, false);
            } else {
                showAuthError(errEl, data.error || 'Login failed. Please try again.');
            }
        } catch {
            showAuthError(errEl, 'Cannot reach server. Please try again.');
        }
    });

    // Sign-up via server
    document.getElementById('authSignupForm')?.addEventListener('submit', async e => {
        e.preventDefault();
        const username = document.getElementById('authSignupUsername').value.trim();
        const password = document.getElementById('authSignupPassword').value;
        const errEl = document.getElementById('authSignupError');
        if (!username || username.length < 3) { showAuthError(errEl, 'Username must be at least 3 characters.'); return; }
        if (!password || password.length < 4) { showAuthError(errEl, 'Password must be at least 4 characters.'); return; }
        try {
            const res = await fetch('/api/auth/signup', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });
            const data = await res.json();
            if (res.ok) {
                // Auto-login after signup
                hideAuthScreen();
                onLoggedIn(username, true);
            } else {
                showAuthError(errEl, data.error || 'Sign-up failed. Please try again.');
            }
        } catch {
            showAuthError(errEl, 'Cannot reach server. Please try again.');
        }
    });

    // Guest — use default 2000 kcal and skip sign-in
    document.getElementById('guestBtn')?.addEventListener('click', () => {
        hideAuthScreen();
        if (!loadUserProfile()) {
            saveUserProfile({ name: 'Guest', age: 25, gender: 'male', heightCm: 170, weightKg: 70, activityLevel: '1.55', goalAdjust: 0, calorieGoal: 2000 });
        }
        onLoggedIn('Guest', false);
        showSuccessToast('Continuing as Guest — 2000 kcal default goal set 🍽️');
    });
}

function showAuthError(el, msg) {
    if (!el) return;
    el.textContent = msg;
    el.style.display = 'block';
    setTimeout(() => { el.style.display = 'none'; }, 5000);
}

// ─── Post-login setup ─────────────────────────────────────────────────────────
function onLoggedIn(username, isNewUser = false) {
    window.currentUser = username;
    // Show new left dashboard sidebar
    const leftSidebar = document.getElementById('leftSidebar');
    if (leftSidebar) leftSidebar.style.display = 'flex';

    // Update sidebar user label
    const sbUser = document.getElementById('sidebarUserName');
    if (sbUser) sbUser.textContent = username;

    // Hide old header auth items that are now redundant
    const headerAuthContainer = document.getElementById('authContainer');
    if (headerAuthContainer) headerAuthContainer.style.display = 'none';
    const greetingDiv = document.getElementById('userGreeting');
    if (greetingDiv) greetingDiv.style.display = 'none';

    if (isNewUser && !loadUserProfile()) {
        setTimeout(() => launchProfileWizard(), 500);
    } else {
        renderCalorieTracker();
        showSuccessToast(`Welcome back, ${username}! 🍛`);
    }
}

// ─── Logout ───────────────────────────────────────────────────────────────────
async function handleNewLogout() {
    try { await fetch('/api/auth/logout'); } catch { }
    window.currentUser = null;

    // Hide dashboard sidebar
    const leftSidebar = document.getElementById('leftSidebar');
    if (leftSidebar) leftSidebar.style.display = 'none';

    // Show header login container for guest view
    const headerAuthContainer = document.getElementById('authContainer');
    if (headerAuthContainer) headerAuthContainer.style.display = 'flex';

    const loginBtn = document.getElementById('loginBtn');
    if (loginBtn) {
        loginBtn.innerHTML = '<i class="fas fa-sign-in-alt"></i> Login';
        loginBtn.classList.remove('btn-primary');
        loginBtn.classList.add('btn-secondary');
    }

    showSuccessToast('Logged out. See you soon! 👋');
    setTimeout(() => showAuthScreen(), 600);
}

// ─── Profile Wizard ───────────────────────────────────────────────────────────
let _wizardProfile = {};

function launchProfileWizard() {
    const el = document.getElementById('profileWizard');
    if (el) el.style.display = 'flex';
    setWizardStep(1);
}

function setWizardStep(step) {
    for (let i = 1; i <= 4; i++) {
        const sEl = document.getElementById(`wizardStep${i}`);
        const dEl = document.querySelector(`.wizard-dot[data-step="${i}"]`);
        if (sEl) sEl.style.display = i === step ? 'block' : 'none';
        if (dEl) {
            dEl.classList.remove('active', 'done');
            if (i < step) dEl.classList.add('done');
            if (i === step) dEl.classList.add('active');
        }
    }
}

function wizardNext(currentStep) {
    if (currentStep === 1) {
        const age = parseInt(document.getElementById('wAge').value);
        const gender = document.getElementById('wGender').value;
        if (!age || age < 10 || age > 100) { alert('Please enter a valid age (10–100).'); return; }
        if (!gender) { alert('Please select your gender.'); return; }
        _wizardProfile.name = document.getElementById('wName').value.trim() || window.currentUser;
        _wizardProfile.age = age;
        _wizardProfile.gender = gender;
        setWizardStep(2);
    } else if (currentStep === 2) {
        const h = parseFloat(document.getElementById('wHeight').value);
        const w = parseFloat(document.getElementById('wWeight').value);
        if (!h || h < 100 || h > 250) { alert('Please enter a valid height (100–250 cm).'); return; }
        if (!w || w < 30 || w > 300) { alert('Please enter a valid weight (30–300 kg).'); return; }
        _wizardProfile.heightCm = h;
        _wizardProfile.weightKg = w;
        setWizardStep(3);
    } else if (currentStep === 3) {
        const act = document.querySelector('input[name="wActivity"]:checked');
        if (!act) { alert('Please select your activity level.'); return; }
        _wizardProfile.activityLevel = act.value;
        setWizardStep(4);
    }
}

function wizardBack(step) {
    if (step > 1) {
        setWizardStep(step - 1);
        const r = document.getElementById('wizardResult');
        const c = document.getElementById('wizardConfirmRow');
        const b = document.getElementById('wizardCalcBtn');
        if (r) r.style.display = 'none';
        if (c) c.style.display = 'none';
        if (b) b.style.display = 'inline-flex';
    }
}

function wizardCalculate() {
    const goalEl = document.querySelector('input[name="wGoal"]:checked');
    if (!goalEl) { alert('Please select your goal.'); return; }
    _wizardProfile.goalAdjust = parseInt(goalEl.value) || 0;
    const { bmr, tdee, goal } = calculateTDEE(_wizardProfile);
    _wizardProfile.calorieGoal = goal;

    const resEl = document.getElementById('wizardResult');
    const valEl = document.getElementById('wizardResultValue');
    const subEl = document.getElementById('wizardResultSub');
    const conRow = document.getElementById('wizardConfirmRow');
    const calcBtn = document.getElementById('wizardCalcBtn');

    valEl.textContent = `${goal} kcal`;
    const label = _wizardProfile.goalAdjust < 0 ? '🔻 Fat Loss' :
        _wizardProfile.goalAdjust > 0 ? '🔺 Lean Gain' : '⚖️ Maintenance';
    subEl.innerHTML = `BMR: <strong>${bmr} kcal</strong> &nbsp;|&nbsp; TDEE: <strong>${tdee} kcal</strong> &nbsp;|&nbsp; Goal: <strong>${label}</strong>`;
    resEl.style.display = 'block';
    conRow.style.display = 'block';
    if (calcBtn) calcBtn.style.display = 'none';
}

function wizardConfirm() {
    saveUserProfile(_wizardProfile);
    document.getElementById('profileWizard').style.display = 'none';
    renderCalorieTracker();
    showSuccessToast(`Daily goal set: ${_wizardProfile.calorieGoal} kcal 🎯`);
}

// ─── Calorie Tracker & Sidebar ────────────────────────────────────────────────

function renderCalorieTracker() {
    const log = getTodayLog();
    const goal = getCalorieGoal();
    let eaten = 0, p = 0, c = 0, f = 0;

    log.forEach(e => {
        eaten += e.kcal || 0;
        p += e.protein || 0;
        c += e.carbs || 0;
        f += e.fat || 0;
    });

    const remaining = goal - eaten;
    const pct = Math.min(100, (eaten / goal) * 100);

    // Update Sidebar
    const sbEaten = document.getElementById('sidebarEaten');
    const sbGoal = document.getElementById('sidebarGoal');
    const sbVal = document.getElementById('sidebarKcalLeftValue');
    const sbLbl = document.getElementById('sidebarKcalLeftLabel');
    const sbCircle = document.getElementById('sidebarCircleFill');
    const sbSvg = document.querySelector('.circular-chart-sidebar');

    if (sbEaten) sbEaten.textContent = Math.round(eaten);
    if (sbGoal) sbGoal.textContent = goal;
    if (sbVal) sbVal.textContent = Math.abs(Math.round(remaining));
    if (sbLbl) {
        sbLbl.textContent = remaining >= 0 ? 'Remaining' : 'Over Goal!';
        sbLbl.parentElement.classList.toggle('over', remaining < 0);
    }

    if (sbCircle) {
        sbCircle.style.strokeDasharray = `${pct}, 100`;
    }
    if (sbSvg) {
        sbSvg.classList.remove('warn', 'over');
        if (pct >= 100) sbSvg.classList.add('over');
        else if (pct >= 80) sbSvg.classList.add('warn');
    }

    // Update Macros
    const mp = document.getElementById('sidebarMacroP');
    const mc = document.getElementById('sidebarMacroC');
    const mf = document.getElementById('sidebarMacroF');
    if (mp) mp.textContent = `${Math.round(p)}g`;
    if (mc) mc.textContent = `${Math.round(c)}g`;
    if (mf) mf.textContent = `${Math.round(f)}g`;

    renderMealLog();
}

// ─── Meal Log ─────────────────────────────────────────────────────────────────
function renderMealLog() {
    const log = getTodayLog();
    const content = document.getElementById('mealLogContent');
    if (!content) return;
    if (!log.length) {
        content.innerHTML = '<p style="color:var(--text-muted);text-align:center;padding:1rem;">No meals logged yet. Start scanning! 🍽️</p>';
        return;
    }
    const grouped = {};
    MEAL_ORDER.forEach(m => { grouped[m] = []; });
    log.forEach((e, i) => { const m = MEAL_ORDER.includes(e.meal) ? e.meal : 'Snack'; grouped[m].push({ ...e, _i: i }); });

    let html = '';
    MEAL_ORDER.forEach(meal => {
        const entries = grouped[meal];
        if (!entries.length) return;
        const total = entries.reduce((s, e) => s + (e.kcal || 0), 0);
        html += `<div class="meal-group"><div class="meal-group-title">${MEAL_EMOJIS[meal]} ${meal}</div>`;
        entries.forEach(e => {
            html += `<div class="meal-log-item">
                ${e.image ? `<img src="${e.image}" class="meal-thumb" style="width: 40px; height: 40px; border-radius: 6px; object-fit: cover; margin-right: 12px; border: 1px solid var(--glass-border);">` : ''}
                <div style="flex: 1; display: flex; flex-direction: column; overflow: hidden;">
                    <span class="meal-dish" title="${e.dish}" style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-weight: 500;">${e.dish}</span>
                    <span class="meal-macros" style="font-size: 0.75rem; color: var(--text-muted);">P:${e.protein || 0}g C:${e.carbs || 0}g F:${e.fat || 0}g</span>
                </div>
                <span class="meal-kcal" style="font-weight: 600; color: var(--primary-color); margin: 0 10px;">${Math.round(e.kcal)} kcal</span>
                <button class="meal-remove" onclick="removeLogEntry(${e._i})" title="Remove" style="background: none; border: none; color: var(--text-muted); cursor: pointer; padding: 5px;">✕</button>
            </div>`;
        });
        html += `<div class="meal-group-total" style="font-size: 0.85rem; text-align: right; color: var(--text-secondary); margin-top: 5px; padding-right: 35px;">${Math.round(total)} kcal total</div></div>`;
    });
    content.innerHTML = html;
}

function addToLog(entry) {
    const log = getTodayLog();
    log.push(entry);
    saveTodayLog(log);
    renderCalorieTracker();
}

function removeLogEntry(index) {
    const log = getTodayLog();
    log.splice(index, 1);
    saveTodayLog(log);
    renderCalorieTracker();
    renderMealLog();
}

function resetDailyLog() {
    if (!confirm('Reset all meals for today?')) return;
    localStorage.removeItem(getTodayKey());
    renderCalorieTracker();
    renderMealLog();
    showSuccessToast("Today's log cleared ♻️");
}

// ─── Tracker toggle button ────────────────────────────────────────────────────
function setupTrackerToggle() {
    document.getElementById('resetDayBtn')?.addEventListener('click', resetDailyLog);
    document.getElementById('sidebarLogoutBtn')?.addEventListener('click', handleNewLogout);
}

// ─── Integration: called from app.js displayResults() ────────────────────────
/**
 * Call this after every successful scan or search to log the meal automatically.
 * @param {Object} data - Full API result object
 */
function logScanToTracker(data) {
    const nut = data.nutrition?.nutrition;
    if (!nut) return;

    // Fix casing for mapping to MEAL_ORDER
    let rawMeal = (document.getElementById('sessionSelect') || {}).value || 'snack';
    const meal = rawMeal.charAt(0).toUpperCase() + rawMeal.slice(1).toLowerCase();

    // Grab the current preview image if available
    const previewImg = document.getElementById('previewImg');
    const image = previewImg ? previewImg.src : null;

    const entry = {
        dish: data.predicted_class || 'Unknown',
        kcal: Math.round(parseFloat(nut.calories) || 0),
        protein: Math.round(parseFloat(nut.protein_g || nut.protein) || 0),
        carbs: Math.round(parseFloat(nut.carbs_g || nut.carbohydrates) || 0),
        fat: Math.round(parseFloat(nut.fats_g || nut.fat) || 0),
        meal,
        image,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };
    addToLog(entry);
    showSuccessToast(`+${entry.kcal} kcal logged to ${meal} 📝`);
}

// ─── Entry point (called from app.js DOMContentLoaded) ───────────────────────
function initAuthAndTracker() {
    setupAuthScreenListeners();
    setupTrackerToggle();

    // Override the existing loginBtn handler to use new full-page flow
    const loginBtn = document.getElementById('loginBtn');
    if (loginBtn) {
        // Remove old listeners by replacing node
        const newBtn = loginBtn.cloneNode(true);
        loginBtn.parentNode.replaceChild(newBtn, loginBtn);
        newBtn.addEventListener('click', () => {
            if (window.currentUser) handleNewLogout();
            else showAuthScreen();
        });
    }

    // Start the auth check flow (async – shows auth screen or app)
    initAppFlow();
}

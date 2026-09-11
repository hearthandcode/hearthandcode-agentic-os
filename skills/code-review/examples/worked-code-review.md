# Worked Code Review — User Registration Endpoint

**Diff size:** 127 lines across 3 files (controller, service, model).
**Goal:** Identify all issues before merging.

---

## Setup

Files under review:
- `app/controllers/users_controller.rb` (+42/-8)
- `app/services/user_registration.rb` (+55/-0)
- `app/models/user.rb` (+30/-2)

---

## Review Output

### Finding #1: SQL injection in `UserRegistration#create`
- **Severity:** BLOCKING
- **Location:** `app/services/user_registration.rb`, line 23
- **Code:** `User.where("email = '#{params[:email]}'")`
- **Evidence:** String interpolation of user input into a SQL WHERE clause. An attacker can supply `' OR 1=1--` as the email to bypass authentication.
- **Impact:** Unauthenticated access to any user account.
- **Recommendation:** Use parameterized queries: `User.where(email: params[:email])`

### Finding #2: Off-by-one in max login attempts
- **Severity:** MINOR
- **Location:** `app/services/user_registration.rb`, line 41
- **Code:** `attempts > MAX_ATTEMPTS` where MAX_ATTEMPTS = 5
- **Evidence:** On the 5th attempt, `attempts` increments to 5, then `5 > 5` is false — the user gets a 6th attempt. The check should be `attempts >= MAX_ATTEMPTS`.
- **Impact:** Users get one extra login attempt beyond the intended limit. Low security impact but behavioral mismatch.
- **Recommendation:** Change `>` to `>=`.

### Finding #3: Missing email format validation
- **Severity:** MAJOR
- **Location:** `app/models/user.rb`, line 12
- **Evidence:** The model validates `presence: true` for email but has no format validation. An input like "not-an-email" passes.
- **Impact:** Invalid data enters the system.
- **Recommendation:** Add `format: { with: URI::MailTo::EMAIL_REGEXP }` to the email validation.

### Finding #4: No rate limiting on registration endpoint
- **Severity:** MAJOR
- **Location:** `app/controllers/users_controller.rb`, line 8
- **Evidence:** The `create` action has no rate limiting. An attacker can script account creation.
- **Impact:** Account enumeration, spam accounts, resource exhaustion.
- **Recommendation:** Add rate limiting middleware (e.g., `rack-attack`) before deploying.

### Finding #5: Hardcoded sender email
- **Severity:** SUGGESTION
- **Location:** `app/services/user_registration.rb`, line 50
- **Code:** `from: 'sender'`
- **Evidence:** Sender email hardcoded instead of using a configuration variable.
- **Impact:** Environment-specific deployments would need a code change to update the sender.
- **Recommendation:** Move sender email to a configuration constant or environment variable.

---

## Positive Notes

- The service object pattern is well-chosen — separating registration logic from the controller keeps responsibilities clear.
- Error handling is present for all failure cases (duplicate email, invalid params, database error).
- The test file (not shown in diff) is mentioned in the PR description with 8 test cases covering all paths.

---

## Quality Checklist

- [x] Every line of the diff was read
- [x] Blocking findings have exploit paths
- [x] Major findings have locations and recommendations
- [x] Pre-existing issues are separated from diff issues
- [x] Positive notes are included
- [ ] I checked for the same pattern in similar files (done: no other SQL injection sites found)
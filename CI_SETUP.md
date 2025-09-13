# CI Pipeline Setup Documentation

## Overview
This document describes the GitHub Actions CI pipeline setup for the PharmaLink Django backend project.

## CI Pipeline Configuration

### File: `.github/workflows/ci.yml`
The CI pipeline is configured to run on:
- Push to `main` and `develop` branches
- Pull requests to `main` and `develop` branches

### Pipeline Steps
1. **Checkout code** - Downloads the repository code
2. **Set up Python 3.12** - Installs Python 3.12 on the GitHub runner
3. **Cache pip dependencies** - Caches pip dependencies for faster builds
4. **Install dependencies** - Installs packages from `requirements.txt`
5. **Run database migrations** - Creates and applies database migrations
6. **Run Django tests** - Executes all Django test cases
7. **Check code quality** - Runs Django system checks

## Test Coverage

### User App Tests (`apps/users/tests.py`)
- **UserModelTest**: Tests for user model creation and validation
  - `test_create_user()` - Tests regular user creation
  - `test_create_superuser()` - Tests superuser creation
  - `test_user_str_representation()` - Tests user string representation

- **UserAPITest**: Tests for user API endpoints
  - `test_user_creation_via_api()` - Tests user registration via API
  - `test_user_login_via_api()` - Tests user login via JWT token API

### Pharmacy App Tests (`apps/pharmacies/tests.py`)
- **PharmacyModelTest**: Tests for pharmacy model
  - `test_create_pharmacy()` - Tests pharmacy creation
  - `test_pharmacy_str_representation()` - Tests pharmacy string representation

- **PharmacyAPITest**: Tests for pharmacy API endpoints
  - `test_pharmacy_list_api()` - Tests pharmacy list endpoint
  - `test_pharmacy_detail_api()` - Tests pharmacy detail endpoint

## Model Changes Made

### User Model Updates
- Modified `apps/users/models.py` to use email as the primary authentication field
- Removed username field and set `USERNAME_FIELD = 'email'`
- Added custom `UserManager` for email-based authentication
- Updated `apps/users/serializers.py` to work with email-only authentication
- Updated `apps/users/views.py` and `apps/users/urls.py` for email-based lookups

## Running Tests Locally

To run the tests locally before pushing to GitHub:

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test

# Check for any issues
python manage.py check
```

## Expected CI Results

When the CI pipeline runs successfully, you should see:
- ✅ All 9 tests passing
- ✅ No Django system check issues
- ✅ Database migrations applied successfully
- ✅ Dependencies installed without errors

## Troubleshooting

If the CI pipeline fails:
1. Check that all tests pass locally
2. Verify that `requirements.txt` contains all necessary dependencies
3. Ensure database migrations are up to date
4. Check for any linting errors using `python manage.py check`

## Benefits

This CI setup provides:
- **Automated testing** on every code push
- **Early error detection** before code reaches production
- **Consistent testing environment** across all developers
- **Quality assurance** for the backend codebase
- **Confidence in deployments** knowing all tests pass

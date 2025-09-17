# PharmaLink Backend Deployment Guide

## Overview

This guide covers the deployment process for the PharmaLink Backend Django application, including staging and production environments on Render.

## Architecture

- **Staging Environment**: `pharmalink-backend-staging.onrender.com`
- **Production Environment**: `pharmalink-backend.onrender.com`
- **CI/CD Pipeline**: GitHub Actions
- **Database**: PostgreSQL (Render managed)
- **Static Files**: WhiteNoise + Render CDN

## Environment Setup

### 1. GitHub Secrets Configuration

Configure the following secrets in your GitHub repository settings:

```
RENDER_API_KEY=your_render_api_key
RENDER_STAGING_SERVICE_ID=your_staging_service_id
RENDER_PRODUCTION_SERVICE_ID=your_production_service_id
```

### 2. Render Service Configuration

#### Staging Service
- **Name**: pharmalink-backend-staging
- **Environment**: Staging
- **Branch**: develop
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn pharmacy_project.wsgi:application`

#### Production Service
- **Name**: pharmalink-backend
- **Environment**: Production
- **Branch**: main
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn pharmacy_project.wsgi:application`

### 3. Environment Variables

#### Staging Environment Variables
```
SECRET_KEY=your_staging_secret_key
DATABASE_URL=postgresql://user:pass@host:port/dbname
DEBUG=False
DJANGO_SETTINGS_MODULE=pharmacy_project.settings_staging
```

#### Production Environment Variables
```
SECRET_KEY=your_production_secret_key
DATABASE_URL=postgresql://user:pass@host:port/dbname
DEBUG=False
DJANGO_SETTINGS_MODULE=pharmacy_project.settings_production
```

## Deployment Process

### 1. Staging Deployment

Staging deployments are triggered automatically when code is pushed to the `develop` branch.

**Process:**
1. Push code to `develop` branch
2. GitHub Actions runs tests
3. If tests pass, deployment to staging occurs
4. Staging environment is validated

**Manual Staging Deployment:**
```bash
git checkout develop
git pull origin develop
git push origin develop
```

### 2. Production Deployment

Production deployments are triggered automatically when code is pushed to the `main` branch.

**Process:**
1. Merge `develop` to `main` branch
2. GitHub Actions runs tests
3. If tests pass, deployment to production occurs
4. Production environment is validated

**Manual Production Deployment:**
```bash
git checkout main
git pull origin main
git merge develop
git push origin main
```

## CI/CD Pipeline Details

### Test Suite
- **Django Tests**: `python manage.py test`
- **Pytest Tests**: `pytest --cov=apps`
- **Coverage Reports**: Generated and uploaded to Codecov
- **Database**: PostgreSQL 15 for testing
- **Python Version**: 3.12

### Deployment Conditions
- ✅ All tests must pass
- ✅ No system check errors
- ✅ Code coverage above threshold
- ✅ Database migrations successful

### Pipeline Stages

1. **Test Stage**
   - Install dependencies
   - Run database migrations
   - Execute Django tests
   - Run pytest with coverage
   - Upload coverage reports

2. **Staging Deployment** (develop branch only)
   - Deploy to Render staging
   - Verify deployment success

3. **Production Deployment** (main branch only)
   - Deploy to Render production
   - Verify deployment success

## Environment Validation

### Staging Environment
- Mirrors production configuration
- Uses staging-specific settings
- Includes additional logging
- More permissive CORS settings for testing

### Production Environment
- Optimized for performance
- Strict security settings
- Minimal logging
- Restricted CORS settings

## Monitoring and Logs

### Staging Monitoring
- **Logs**: Available in Render dashboard
- **Health Check**: `/health/` endpoint
- **Metrics**: Basic performance metrics

### Production Monitoring
- **Logs**: Available in Render dashboard
- **Health Check**: `/health/` endpoint
- **Metrics**: Full performance metrics
- **Alerts**: Configured for critical issues

## Troubleshooting

### Common Issues

1. **Deployment Fails**
   - Check GitHub Actions logs
   - Verify all tests pass locally
   - Check environment variables

2. **Database Connection Issues**
   - Verify DATABASE_URL format
   - Check database credentials
   - Ensure database is accessible

3. **Static Files Not Loading**
   - Check STATIC_ROOT configuration
   - Verify WhiteNoise settings
   - Check file permissions

4. **CORS Issues**
   - Verify CORS_ALLOWED_ORIGINS
   - Check frontend URL configuration
   - Test with different browsers

### Debug Commands

```bash
# Test locally with staging settings
python manage.py runserver --settings=pharmacy_project.settings_staging

# Test locally with production settings
python manage.py runserver --settings=pharmacy_project.settings_production

# Run tests with coverage
pytest --cov=apps --cov-report=html

# Check Django configuration
python manage.py check --deploy
```

## Security Considerations

### Staging Environment
- Uses staging-specific secret keys
- More permissive CORS settings
- Additional logging for debugging

### Production Environment
- Uses production secret keys
- Strict CORS settings
- Minimal logging
- Security headers enabled

## Performance Optimization

### Database
- Connection pooling enabled
- Query optimization
- Index optimization

### Static Files
- WhiteNoise compression
- CDN integration
- Cache headers

### Application
- Gunicorn workers
- Memory optimization
- Response compression

## Backup and Recovery

### Database Backups
- Automatic daily backups (Render managed)
- Point-in-time recovery available
- Manual backup creation

### Code Backups
- Git repository serves as backup
- Multiple branch protection
- Tagged releases

## Rollback Procedures

### Staging Rollback
1. Revert to previous commit
2. Push to develop branch
3. Monitor deployment

### Production Rollback
1. Revert to previous commit
2. Push to main branch
3. Monitor deployment
4. Notify stakeholders

## Contact Information

- **Lead Developer**: Alvin
- **Repository**: [GitHub Repository URL]
- **Staging URL**: https://pharmalink-backend-staging.onrender.com
- **Production URL**: https://pharmalink-backend.onrender.com

## Changelog

### Version 1.0.0
- Initial deployment setup
- CI/CD pipeline implementation
- Staging and production environments
- Comprehensive testing suite

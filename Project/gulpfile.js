var gulp = require('gulp');
var minifyCSS = require('gulp-minify-css');
var uglify = require('gulp-uglify');

gulp.task('minify-css',function () {
  return gulp.src('HoneyPot/static/css/*.css').pipe(minifyCSS()).pipe(gulp.dest('HoneyPot/static/build/css'))
});

gulp.task('uglify',function () {
  return gulp.src('HoneyPot/static/js/*.js').pipe(uglify()).pipe(gulp.dest('HoneyPot/static/build/js'))
});

gulp.task('default', ['minify-css', 'uglify'])

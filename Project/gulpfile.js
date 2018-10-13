var gulp = require('gulp');
var minifyCSS = require('gulp-minify-css');
var uglify = require('gulp-uglify');

gulp.task('minify-css',function () {
  return gulp.src('HoneyPot/templates/HoneyPot/css/*.css').pipe(minifyCSS()).pipe(gulp.dest('HoneyPot/templates/HoneyPot/build/css'))
});

gulp.task('uglify',function () {
  return gulp.src('HoneyPot/templates/HoneyPot/js/*.js').pipe(uglify()).pipe(gulp.dest('HoneyPot/templates/HoneyPot/build/js'))
});

gulp.task('default', ['minify-css', 'uglify'])

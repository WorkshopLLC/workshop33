var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var minify = require('gulp-minify-css');
var merge = require('merge-stream');


gulp.task('styles', function () {
    if (process.env.NODE_ENV === "development") {
        var cssStream = gulp.src('./styles/vendor/css/main.css')
            .pipe(sass())
            .pipe(concat('scss-files.css'))
        ;
        var scssStream = gulp.src('./styles/main.scss')
            .pipe(sass())
            .pipe(concat('scss-files.scss'))
        ;

        return merge(scssStream, cssStream)
            .pipe(concat('styles.css'))
            .pipe(minify())
            .pipe(gulp.dest('../../static/home/styles'));
    }
    else {
        var cssStream = gulp.src('./styles/vendor/css/main.css')
            .pipe(sass())
            .pipe(concat('scss-files.css'))
        ;
        var scssStream = gulp.src('./styles/main.scss')
            .pipe(sass())
            .pipe(concat('scss-files.scss'))
        ;

        return merge(scssStream, cssStream)
            .pipe(concat('styles.css'))
            .pipe(minify())
            .pipe(gulp.dest('../../static/home/styles'));
    }
});


gulp.task('default', ['styles']);

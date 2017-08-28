'use strict';

var gulp = require('gulp'),
    watch = require('gulp-watch'),
    autoprefix = require('gulp-autoprefixer'),
    less = require('gulp-less'),
    minifyCSS = require('gulp-clean-css'),
    rename = require('gulp-rename'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    gulpIgnore = require('gulp-ignore'),
    rigger = require('gulp-rigger'),
    imageop = require('gulp-image-optimization'),
    rimraf = require('rimraf'),
    browserSync = require("browser-sync"),
    reload = browserSync.reload,
    cleanCSS = require('gulp-clean-css');

var path = {
    build: { // production
        js: 'build/js/',
        jsPages: 'build/js/separate/',
        jsLib: 'build/js/lib/',
        css: 'build/css/',
        cssLib: 'build/css/lib/',
        cssPages: 'build/css/separate/pages/',
        img: 'build/img/',
        fonts: 'build/fonts/'
    },
    src: { // development
        jsPlugins: 'src/js/plugins.js',
        jsLib: 'src/js/lib/**/*.*',
        jsPages: 'src/js/separate/**/*.*',
        js: 'src/js/app/app.js',
        style: 'src/styles/main.less',
        styleLib: 'src/styles/lib/*.css',
        stylePages: 'src/styles/pages/*.less',
        styleLibFiles: 'src/styles/lib/**/*.*',
        styleLibIgnore: '!src/styles/lib/*.css',
        img: 'src/img/**/*.*',
        fonts: 'src/fonts/**/*.*'
    },
    watch: {
        js: 'src/js/**/*.js',
        style: 'src/styles/**/*.*',
        img: 'src/img/**/*.*',
        fonts: 'src/fonts/**/*.*'
    },
    clean: './build'
};


/* =====================================================
    JS
    ===================================================== */

gulp.task('jsPlugins:build', function () {
    return gulp.src(path.src.jsPlugins)
        .pipe(rigger())
        .pipe(uglify())
        .pipe(gulp.dest(path.build.js))
        .pipe(reload({stream: true}));
});

gulp.task('jsLib:build', function () {
    return gulp.src(path.src.jsLib)
        .pipe(uglify())
        .pipe(gulp.dest(path.build.jsLib))
        .pipe(reload({stream: true}));
});

gulp.task('jsPages:build', function () {
    return gulp.src(path.src.jsPages)
        .pipe(uglify())
        .pipe(gulp.dest(path.build.jsPages))
        .pipe(reload({stream: true}));
});

gulp.task('js:build', function () {
    return gulp.src(path.src.js)
        .pipe(rigger())
        .pipe(uglify())
        .pipe(gulp.dest(path.build.js))
        .pipe(reload({stream: true}));
});


/* =====================================================
    STYLES
    ===================================================== */

gulp.task('style:build:main', function () {
    return gulp.src(path.src.style)
        .pipe(less())
        .pipe(autoprefix({
            browsers: ['last 30 versions', '> 1%', 'ie 8', 'ie 9'],
            cascade: true
        }))
        .pipe(rename('main.source.css'))
        .pipe(gulp.dest(path.build.css))
        .pipe(reload({stream: true}));
});

gulp.task('style:build', function () {
    return gulp.src(path.src.style)
        .pipe(less())
        .pipe(autoprefix({
            browsers: ['last 30 versions', '> 1%', 'ie 8', 'ie 9'],
            cascade: true
        }))
        .pipe(minifyCSS())
        .pipe(gulp.dest(path.build.css))
        .pipe(reload({stream: true}));
});

gulp.task('styleLib:build', function () {
    return gulp.src(path.src.styleLib)
        .pipe(autoprefix({
            browsers: ['last 30 versions', '> 1%', 'ie 8', 'ie 9'],
            cascade: true
        }))
        .pipe(minifyCSS())
        .pipe(gulp.dest(path.build.cssLib))
        .pipe(reload({stream: true}));
});

gulp.task('styleLibFiles:build', function () {
    return gulp.src([path.src.styleLibFiles, path.src.styleLibIgnore])
        .pipe(gulp.dest(path.build.cssLib))
});

gulp.task('stylePages:build', function () {
    return gulp.src(path.src.stylePages)
    	.pipe(less())
        .pipe(autoprefix({
            browsers: ['last 30 versions', '> 1%', 'ie 8', 'ie 9'],
            cascade: true
        }))
        .pipe(minifyCSS())
        .pipe(gulp.dest(path.build.cssPages))
        .pipe(reload({stream: true}));
});



gulp.task('style:build:source', function () {
    gulp.src('./src/styles/**/*.less')
        .pipe(less())
        .pipe(autoprefix({
            browsers: ['last 30 versions', '> 1%', 'ie 8', 'ie 9'],
            cascade: true
        }))
        .pipe(gulp.dest('./build/css/separate/'))
    ;
});

gulp.task('style:build:minify', function () {
    gulp.src('./src/styles/**/*.less')
        .pipe(less())
        .pipe(autoprefix({
            browsers: ['last 30 versions', '> 1%', 'ie 8', 'ie 9'],
            cascade: true
        }))
        .pipe(cleanCSS())
        .pipe(rename({suffix: ".min"}))
        .pipe(gulp.dest('./build/css/separate/'))
    ;
});

/* =====================================================
    IMAGES
    ===================================================== */

gulp.task('image:build', function (cb) {
    gulp.src(path.src.img)
        .pipe(imageop({
            optimizationLevel: 5,
            progressive: true,
            interlaced: true
        }))
        .pipe(gulp.dest(path.build.img)).on('end', cb).on('error', cb);
});


/* =====================================================
    FONTS
    ===================================================== */

gulp.task('fonts:build', function() {
    return gulp.src(path.src.fonts)
		.pipe(gulp.dest(path.build.fonts))
});


/* =====================================================
    BUILD TASK
    ===================================================== */

gulp.task('build', [
    'fonts:build',
    'jsPlugins:build',
    'jsLib:build',
    'jsPages:build',
    'js:build',
    'style:build',
    'style:build:main',
    'stylePages:build',
    'styleLib:build',
    'styleLibFiles:build',
    'image:build'
]);


/* =====================================================
    WATCH
    ===================================================== */

gulp.task('watch', function(){
    watch([path.watch.style], function(event, cb) {
        gulp.start('style:build');
    });
    watch([path.watch.style], function(event, cb) {
        gulp.start('style:build:main');
    });
    watch([path.watch.style], function(event, cb) {
        gulp.start('styleLib:build');
    });
    watch([path.watch.style], function(event, cb) {
        gulp.start('styleLibFiles:build');
    });
    watch([path.watch.style], function(event, cb) {
        gulp.start('stylePages:build');
    });
    watch([path.watch.js], function(event, cb) {
        gulp.start('jsPlugins:build');
    });
    watch([path.watch.js], function(event, cb) {
        gulp.start('jsLib:build');
    });
    watch([path.watch.js], function(event, cb) {
        gulp.start('jsPages:build');
    });
    watch([path.watch.js], function(event, cb) {
        gulp.start('js:build');
    });
    watch([path.watch.img], function(event, cb) {
        gulp.start('image:build');
    });
    watch([path.watch.fonts], function(event, cb) {
        gulp.start('fonts:build');
    });
});

/* =====================================================
    CLEAN PRODUCTION
    ===================================================== */

gulp.task('clean', function (cb) {
    rimraf(path.clean, cb);
});

/* =====================================================
    DEFAULT TASK
    ===================================================== */

gulp.task('default', ['build', 'watch']);
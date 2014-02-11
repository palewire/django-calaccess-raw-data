// Generated on 2014-02-03 using generator-newsapp 0.2.14
'use strict';

module.exports = function (grunt) {

  // configurable paths
  var yeoman = {
    app: 'app',
    dist: 'dist'
  };

  // load all grunt tasks from package.json
  require('load-grunt-tasks')(grunt);

  grunt.initConfig({
    yeoman: yeoman,
    pkg: grunt.file.readJSON('package.json'),
    watch: {
      options: {
        livereload: true
      },
      css: {
        files: ['assets/styles/scss/*.scss'],
        
        tasks: ['sass'],
      },
      src: {
        files: ['templates/**/*.html', 'assets/scripts/**/*.js', 'Gruntfile.js'],
      }
    }, // watch

    sass: { // Task
      dist: { // Target
        files: { // Dictionary of files
          // 'dest': 'source'
          'assets/styles/main.css': 'assets/styles/scss/main.scss'
          
        }
      }
    },
    concat: {
      options: {
        // define a string to put between each file in the concatenated output
        separator: ';'
      },
      dist: {
        // files to concatenate
      }
    },
    'bower-install': {
      target: {
        src: ['templates/index.html'],
        ignorePath: ['templates'],
      }
    },
    jshint: {
      // define the files to lint
      files: ['Gruntfile.js', 'app/scripts/*.js'],
      // configure JSHint (documented at http://www.jshint.com/docs/)
      options: {
          // more options here if you want to override JSHint defaults
        globals: {
          Handlebars: true,
          L: true,
          jQuery: true,
          console: true,
          module: true
        }
      }
    }
  });

  grunt.registerTask('default', [
    'sass', 
    'watch'
  ]);


}

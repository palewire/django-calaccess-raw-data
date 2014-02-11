'use strict';

var App = App || {};

jQuery(document).ready(function($) {
  console.log('You are ready to build a news app!');
  $('#jquery-version').text($.fn.jquery);
});
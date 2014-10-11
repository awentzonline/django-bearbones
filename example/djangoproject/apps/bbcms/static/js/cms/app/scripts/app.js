'use strict';

angular.module('cmsApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'restangular',
  'jlareau.pnotify',
])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: '/static/js/cms/app/views/contentList.html',
        controller: 'ContentListCtrl'
      })
      .when('/edit/:id', {
        templateUrl: '/static/js/cms/app/views/contentEdit.html',
        controller: 'ContentEditCtrl'
      })
      .when('/create', {
        templateUrl: '/static/js/cms/app/views/contentCreate.html',
        controller: 'ContentCreateCtrl'
      })
      .when('/push', {
        templateUrl: '/static/js/cms/app/views/pushSite.html',
        controller: 'PushSiteCtrl'
      })
      // .otherwise({
      //   redirectTo: '/'
      // });
  })
  .config(['notificationServiceProvider', function(notificationServiceProvider) {

    notificationServiceProvider.setDefaults({
      delay: 1000
    });

  }]);
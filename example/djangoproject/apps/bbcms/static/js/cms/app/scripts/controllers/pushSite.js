'use strict';

angular.module('cmsApp')
  .controller('PushSiteCtrl',
  function ($scope, $routeParams, ContentApi, notificationService) {
    $scope.recentPushes = [];
    $scope.preview = '';
    ContentApi.all('sitepush').getList().then(function (data) {
        $scope.recentPushes = data;
    });

    $scope.fetchPreview = function () {
        notificationService.info('Estimating...');
        ContentApi.all('sitepush').get({estimate:'true'}).then(function (data) { 
            console.log(data);
        });
    };
    $scope.pushSite = function () {
        notificationService.info('Pushing site...');
        
        notificationService.success('Pushed site');
    };
  });

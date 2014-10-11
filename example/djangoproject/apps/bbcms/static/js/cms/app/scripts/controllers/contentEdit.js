'use strict';

angular.module('cmsApp')
  .controller('ContentEditCtrl',
  function ($scope, $routeParams, ContentApi, notificationService) {
    $scope.content = {};
    ContentApi.one('content', $routeParams.id).get().then(function (data) {
        $scope.content = data;
    });
    $scope.saveContent = function () {
        notificationService.info('Saving...');
        $scope.content.save().then(function () {
            notificationService.success('Saved!');
        });
    };
    $scope.publishContent = function () {
        notificationService.info('Publishing...');
        $scope.content.save().then(function (data) {
            notificationService.success('Published');
        });
    };
  });

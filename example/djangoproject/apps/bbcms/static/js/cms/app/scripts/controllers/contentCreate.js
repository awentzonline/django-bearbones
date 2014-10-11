'use strict';

angular.module('cmsApp')
  .controller('ContentCreateCtrl',
  function ($scope, $location, $routeParams, ContentApi, notificationService) {
    $scope.newTitle = '';

    $scope.createContent = function (ctype) {
        if (!$scope.newTitle) {
            //alert('Title is required');
            notificationService.error('Title is required');
            return;
        }
        var content = {
            title: $scope.newTitle
        };
        notificationService.info('Creating...');
        ContentApi.all('content').post(content, {ctype: ctype}).then(
            function (data) {
                $scope.content = data;
                notificationService.success('Created!');
                $location.path('/edit/' + data.id);
            }
        );
    };
  });

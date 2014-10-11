'use strict';

angular.module('cmsApp')
  .controller('ContentListCtrl', function ($scope, ContentApi) {
    $scope.contentList = [];
    ContentApi.all('content').getList().then(function (data) {
        $scope.contentList = data;
    });
  });

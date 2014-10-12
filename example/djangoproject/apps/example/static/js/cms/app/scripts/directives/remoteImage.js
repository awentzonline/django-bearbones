'use strict';


angular.module('cmsApp')
  .directive('remoteImage', function () {
    return {
      restrict: 'E',
      scope: {
        image: '='
      },
      templateUrl: '/cms/templates/directives/remote_image.html'
    };
  });

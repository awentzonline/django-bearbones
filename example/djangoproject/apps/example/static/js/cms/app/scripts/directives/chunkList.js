'use strict';


angular.module('cmsApp')
  .directive('chunkList', function () {
    return {
      restrict: 'E',
      scope: {
        chunks: '=',
        allowedChunks: '=allowed'
      },
      templateUrl: '/cms/templates/directives/chunk_list.html',
      controller: 'ChunkListCtrl'
    };
  });

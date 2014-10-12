'use strict';

angular.module('cmsApp')
  .controller('ChunkListCtrl',
  function ($scope, notificationService, chunkManager) {
    chunkManager.setList($scope.chunks);
    $scope.chunkChoices = chunkManager.getChunkChoices();
    $scope.newChunkType = $scope.chunkChoices[0].type;

    $scope.appendChunk = function (chunkType) {
      var chunk = chunkManager.appendChunk($scope.newChunkType);
      if (!chunk) {
        notificationService.error('Error adding chunk');
      }
    };

    $scope.removeChunk = function (chunkId) {
      chunkManager.removeChunk(chunkId);
    };

    $scope.moveChunkAfter = function (chunkId, otherId) {
      chunkManager.moveChunkAfter(chunkId, otherId);
    };

    $scope.moveChunkBefore = function (chunkId, otherId) {
      chunkManager.moveChunk(chunkId, otherId);
    };
  });

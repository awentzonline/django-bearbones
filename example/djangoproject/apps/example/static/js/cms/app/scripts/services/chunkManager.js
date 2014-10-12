'use strict';


angular.module('cmsApp')
  .factory('chunkManager', function (chunkConfigs) {
    var nextId = 1;
    var chunkList = [];
    var service = {};

    service.setList = function (newChunkList) {
      chunkList = newChunkList;
      if (chunkList.length > 0) {
        var maxId = _.max(_.pluck(newChunkList, 'id'));
        nextId = maxId + 1;
      } else {
        nextId = 1;
      }
    };

    service.appendChunk = function (chunkType) {
      var conf = chunkConfigs[chunkType];
      if (!conf) {
        return null;
      }
      var chunk = angular.copy(conf);
      chunk.id = nextId++;
      chunkList.push(chunk);
      return chunk;
    };

    service.removeChunk = function (chunkId) {
      var chunk = _.find(chunkList, {id: chunkId});
      if (chunk) {
        _.remove(chunkList, chunk);
      }
    };

    service.moveChunkAfter = function (chunkId, otherId) {
      var chunk = _.remove(chunkList, {id: chunkId});
      var otherIndex = _.indexOf(chunkList, {id: otherId});
      if (!chunk || !other) {
        return false;
      }

    };

    service.getChunkChoices = function () {
      return _.map(chunkConfigs, function (value, key) {
        return value;
      });
    };

    return service;
  })
  .constant('chunkConfigs', {
    text: {
      type: 'text',
      verboseName: 'Text',
      data: {    
        body: ''
      }
    },
    image: {
      type: 'image',
      verboseName: 'Image',
      data: {
        image: {
          url: '',
          caption: ''
        }
      }
    }
  });

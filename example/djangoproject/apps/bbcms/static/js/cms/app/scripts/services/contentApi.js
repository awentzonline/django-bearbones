'use strict';


angular.module('cmsApp')
  .factory('ContentApi', function (Restangular, contentApiConfig) {
    return Restangular.withConfig(function (RestangularConfigurer) {
      RestangularConfigurer.setBaseUrl(contentApiConfig.baseUrl);
    });
  })
  .constant('contentApiConfig', {
    baseUrl: '/cms/api/v1'
  });


angular.module('cmsApp')
  .config(function (RestangularProvider, cmsApiConfig) {
    // This is specific to Django Rest Framework      
    RestangularProvider.setResponseExtractor(function (response, operation, what, url) {
      var newResponse = response;
      if (operation === 'getList') {
        if (typeof response.results !== 'undefined') {
          newResponse = response.results;
          newResponse.metadata = {
            count: response.count,
            next: response.next,
            previous: response.previous
          };
        }
      }
      return newResponse;
    });
    if (cmsApiConfig.requestSuffix) {
      RestangularProvider.setRequestSuffix(cmsApiConfig.requestSuffix);
    }
  })
  .constant('cmsApiConfig', {
    requestSuffix: '/'
  });
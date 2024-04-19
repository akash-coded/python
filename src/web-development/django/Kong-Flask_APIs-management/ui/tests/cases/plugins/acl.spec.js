var HomePage = require('../../util/HomePage');
var Sidebar = require('../../util/Sidebar');
var PluginPage = require('../../util/PluginPage');
var ListPluginsPage = require('../../util/ListPluginsPage');
var KongDashboard = require('../../util/KongDashboard');
var Kong = require('../../util/KongClient');
var PropertyInput = require('../../util/PropertyInput');
var ObjectProperties = require('../../util/ObjectProperties');

var kd = new KongDashboard();

describe('Acl plugin testing:', () => {

  var api;

  beforeAll((done) => {
    kd.start({'--kong-url': 'http://127.0.0.1:8001'}, () => {
      Kong.deleteAllAPIs().then(() => {
        return createAPI();
      }).then((response) => {
        api = response;
        done();
      });
    });
  });

  afterAll((done) => {
    kd.stop(done);
  });

  beforeEach((done) => {
    Kong.deleteAllPlugins().then(done);
  });

  it('should be successfully create acl plugin for All APIs', (done) => {
    HomePage.visit();
    Sidebar.clickOn('Plugins');
    ListPluginsPage.clickAddButton();
    var inputs = {
      'name': 'acl',
      'api_id': 'All',
      'config-blacklist': ['foo', 'bar']
    };
    ObjectProperties.fillAndSubmit(inputs).then(() => {
      expect(element(by.cssContainingText('div.toast', 'Plugin saved!')).isPresent()).toBeTruthy();
      return Kong.getFirstPlugin();
    }).then((createdPlugin) => {
      expect(createdPlugin.name).toEqual('acl');
      expect(createdPlugin.api_id).toBeUndefined();
      expect(createdPlugin.config).toEqual({'blacklist': ['foo', 'bar']});

      // making sure form got reinitialized.
      expect(PropertyInput.getElement('config-blacklist').isPresent()).toBeFalsy();
      done();
    });
  });

  it('should be successfully create acl plugin for one API', (done) => {
    HomePage.visit();
    Sidebar.clickOn('Plugins');
    ListPluginsPage.clickAddButton();
    var inputs = {
      'name': 'acl',
      'api_id': api.name,
      'config-whitelist': ['foo']
    };
    ObjectProperties.fillAndSubmit(inputs).then(() => {
      expect(element(by.cssContainingText('div.toast', 'Plugin saved!')).isPresent()).toBeTruthy();
      return Kong.getFirstPlugin();
    }).then((createdPlugin) => {
      expect(createdPlugin.name).toEqual('acl');
      expect(createdPlugin.api_id).toEqual(api.id);
      expect(createdPlugin.config).toEqual({'whitelist': ['foo']});
      done();
    });
  });

  it('should be possible to edit a previously created acl plugin', (done) => {
    Kong.createPlugin({
      name: 'acl',
      config: {blacklist: ['foo', 'bar']}
    }).then((createdPlugin) => {
      PluginPage.visit(createdPlugin.id);
      var inputs = {
        'config-blacklist': '',
        'config-whitelist': ['admin']
      };
      return ObjectProperties.fillAndSubmit(inputs);
    }).then(() => {
      expect(element(by.cssContainingText('div.toast', 'Plugin saved!')).isPresent()).toBeTruthy();
      return Kong.getFirstPlugin();
    }).then((updatedPlugin) => {
      expect(updatedPlugin.name).toEqual('acl');
      expect(updatedPlugin.api_id).toBeUndefined();
      expect(updatedPlugin.config).toEqual({'whitelist': ['admin'], 'blacklist': {}});
      done();
    });
  });

  function createAPI() {
    if (process.env.KONG_VERSION === '0.9') {
      return Kong.createAPI({
        'name': 'api_for_acl',
        'request_path': '/api_for_acl',
        'upstream_url': 'http://foo'
      });
    }

    if (['0.10', '0.11', '0.12', '0.13'].includes(process.env.KONG_VERSION)) {
      return Kong.createAPI({
        name: 'api_for_acl',
        hosts: ['host1.com', 'host2.com'],
        uris: ['/1.0', '/2.0'],
        methods: ['GET', 'POST'],
        upstream_url: 'http://upstream.loc',
      });
    }

    throw new Error('Kong version not supported in unit tests.')
  }

});

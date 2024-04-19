var HomePage = require('../../util/HomePage');
var Sidebar = require('../../util/Sidebar');
var PluginPage = require('../../util/PluginPage');
var ListPluginsPage = require('../../util/ListPluginsPage');
var KongDashboard = require('../../util/KongDashboard');
var Kong = require('../../util/KongClient');
var PropertyInput = require('../../util/PropertyInput');
var ObjectProperties = require('../../util/ObjectProperties');

var kd = new KongDashboard();

describe('Correlation ID plugin testing', () => {

  beforeAll((done) => {
    kd.start({'--kong-url': 'http://127.0.0.1:8001'}, () => {
      done();
    });
  });

  afterAll((done) => {
    kd.stop(done);
  });

  beforeEach((done) => {
    Kong.deleteAllPlugins().then(done);
  });

  it("should display default value for generator field", (done) => {
    HomePage.visit();
    Sidebar.clickOn('Plugins');
    ListPluginsPage.clickAddButton();
    ObjectProperties.fill({'name': 'correlation-id'}).then(() => {
      expect(PropertyInput.get('config-generator')).toEqual('uuid#counter');
      done();
    });
  });

});

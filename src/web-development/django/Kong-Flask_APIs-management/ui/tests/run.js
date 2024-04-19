#!/usr/bin/env node

var execSync = require('child_process').execSync;
var terminal = require('../lib/terminal');
var request = require('../lib/request');
var semver = require('semver');

terminal.info('------------------------');
terminal.info('-- Updating webdriver --');
terminal.info('------------------------');
execSync('node_modules/.bin/webdriver-manager update', {stdio: 'inherit'});

terminal.info('-------------------');
terminal.info('-- Running tests --');
terminal.info('-------------------');
request.get('http://localhost:8001').then((response) => {
  var version = JSON.parse(response.body).version;
  var kongVersion = semver.major(version) + '.' + semver.minor(version);
  return execSync('KONG_VERSION=' + kongVersion + ' node_modules/.bin/protractor tests/conf.js', {stdio: 'inherit'});
}).catch((error) => {
  process.exit(1);
});

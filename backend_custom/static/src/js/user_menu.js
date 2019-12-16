odoo.define('backend_custom.UserMenu', function (require) {
    "use strict";

    var UserMenu = require('web.UserMenu');

    UserMenu.include({
    	// include class to show db name without debug mode
	    start: function () {
	    	this._super();
	        var self = this;
	        var session = this.getSession();

	        return this._super.apply(this, arguments).then(function () {
	            var topbar_name = session.name;
	            if (!session.debug) {
	                topbar_name = _.str.sprintf("%s (%s)", topbar_name, session.db);
	                self.$('.oe_topbar_name').text(topbar_name);
	            }
	            
	        });
	    },

    });
});
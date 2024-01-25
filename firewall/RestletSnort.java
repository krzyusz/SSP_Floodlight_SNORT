package snort.flood.firewall;

import org.restlet.Context;
import org.restlet.Restlet;
import org.restlet.routing.Router;

import net.floodlightcontroller.restserver.RestletRoutable;


public class RestletSnort implements RestletRoutable {

	@Override
	public Restlet getRestlet(Context context) {
        Router router = new Router(context);
        
        router.attach("/snort/block", StaticSnortBlocker.class);
		return router;
	}

	@Override
	public String basePath() {
        return "/wm/SnortAPI";
	}

}

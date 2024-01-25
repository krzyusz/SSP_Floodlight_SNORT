package snort.flood.firewall;



import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import org.restlet.resource.Post;
import org.restlet.resource.ServerResource;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import net.floodlightcontroller.staticflowentry.StaticFlowEntries;
import net.floodlightcontroller.staticflowentry.StaticFlowEntryPusher;

import net.floodlightcontroller.storage.IStorageSourceService;

/**
 * Simplified Static Entry Pusher Resource that blocks a flow based on src, dst, and proto.
 */
public class StaticSnortBlocker extends ServerResource {
    private static final String TABLE_NAME = "controller_staticflowtableentry";
	protected static Logger log = LoggerFactory.getLogger(StaticSnortBlocker.class);

    /**
     * Accepts a simplified JSON format for flow blocking and pushes it to the database.
     * @param json The flow entry in simplified JSON format.
     * @return A string status message.
     */
    @Post
    public String blockFlow(String json) {
        IStorageSourceService storageSource =
                (IStorageSourceService)getContext().getAttributes().
                get(IStorageSourceService.class.getCanonicalName());
		Map<String, Object> rowValues;

        try {
        	rowValues = StaticFlowEntries.jsonToStorageEntry(json);
			String status = null;

				status = "Entry pushed";            
				storageSource.insertRowAsync(StaticSnortBlocker.TABLE_NAME, rowValues);
			
			return ("{\"status\" : \"" + status + "\"}");
		} catch (IOException e) {
			log.error("Error parsing push flow mod request: " + json, e);
			return "{\"status\" : \"Error! Could not parse flow mod, see log for details.\"}";
		}        
	}


    /**
     * Parses the simplified JSON format to a flow entry map.
     * @param json The flow entry in simplified JSON format.
     * @return A map representing the flow entry.
     * @throws IOException If parsing fails.
     */
//    private Map<String, Object> parseJsonToFlowEntry(String json) throws IOException {
//        Map<String, Object> flowEntry = new HashMap<>();
//        flowEntry.put("src", "10.0.0.1");
//        flowEntry.put("dst", "10.0.0.2");
//        flowEntry.put("proto", "TCP");
//
//        return flowEntry;
//    }
}

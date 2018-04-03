## Building Envelope Data Specification

The following provides the working fields for the Building Envelope data types. All data needs to be in JSON with location data encoded in [GeoJSON](http://geojson.org/). 

### Building Envelope Data Types
The fields marked with an asterisk are already populated when you create the data source for your building in Stae. 

| Field | Data type | Description | Validation | Example
| ---   | --- 		| ---         | ---		   | ---
|id*    | Text      | Includes data about a building's envelope: walls, floors, roofs, fenestrations and doors. | Not empty | "Building Envelope"
|name*  | Text      | Descriptive name of the building being monitored. | Not empty | "City Hall"
|notes* | Text 		| Description or further notes about the vehicle. | Not empty | "Thermal Anaysis of City Hall"
|temperature   | Number (Fahrenheit)      | Reading of temperature value. |  Not empty | "72.43"
|humidity| Number 	| Reading of humidity value | Not empty, percentage: 0 to 1 | "37.56%"
|type| Text | Type of fenestration in a building | enumeration: wall, floor, door, roof, window, skylight | "window"
|room_type| Text | Type of room in a building | Not empty, max character length: 2048 | "court room"
|location_building| Text | Indoor or outdoor location of the temperature sensor | enumeration: interior, exterior | "interior"
|floor| number | Building floor where the temperature sensor exists | Not empty | "4"
|images | Array 	| List of images related to the building or location in the building | Not empty, max character length: 2048 | [https://stae.co/bldg1.jpg, https://stae.co/bldg2.jpg]
|stream | Text 		| URL of the live video feed for the building camera. | Not empty, max character length: 2048, stream URL exists | https://stae.co/BldgFeed
|location_point | Point 	| Location of where the fenestration exists. | GEOJSON format | {"type": "Point", "coordinates": [-74.0429, 40.744]}
|location_polygon | Polygon 	| Location of the building footprint. | GEOJSON format | {"type": "Polygon", "coordinates": [-74.0429, 40.744], [-74.0431, 40.748], [-74.0429, 40.744]}
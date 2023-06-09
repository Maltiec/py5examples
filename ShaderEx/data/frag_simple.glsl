precision mediump float;

// our texture
uniform sampler2D u_image;
uniform vec2 u_textureSize;
void main() {
	vec2 textCoord = gl_FragCoord.xy / u_textureSize;
	vec2 onePixel = vec2(1.0, 1.0) / u_textureSize;
	gl_FragColor = (
		texture2D(u_image, textCoord + onePixel*vec2(-1.0, -1.0)) +
		texture2D(u_image, textCoord + onePixel*vec2(0.0, -1.0)) + 
		texture2D(u_image, textCoord + onePixel*vec2(1.0, -1.0)) + 
		texture2D(u_image, textCoord + onePixel*vec2(-1.0, 0.0)) + 
		texture2D(u_image, textCoord + onePixel*vec2(0.0,  0.0)) + 
		texture2D(u_image, textCoord + onePixel*vec2(1.0,  0.0)) + 
		texture2D(u_image, textCoord + onePixel*vec2(-1.0, 1.0)) + 
		texture2D(u_image, textCoord + onePixel*vec2(0.0,  1.0)) + 
		texture2D(u_image, textCoord + onePixel*vec2(1.0,  1.0))) / 9.0;
}
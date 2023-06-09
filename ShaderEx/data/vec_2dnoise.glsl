#define GLSLIFY 1
/*
 * The main program
 */
attribute vec3 position;

void main() {
    // Vertex shader output
    gl_Position = vec4(position, 1.0);
}

uniform float uGain; 
uniform float uOffset; 
uniform float uLacunarity; 
uniform float H; 
uniform int uOctaves; 
uniform float uAmp; 
uniform float uPeriod; 
uniform vec3 uTranslate;
in vec3 uv;
 
out vec4 fragColor; 
 
 
float terrain(vec3 p){ 
vec3 point = (p*uPeriod) + uTranslate; 
 
 
float noise = noise1(point); 
float signal = noise; 
signal = abs(signal); // ridge the base map at 0 
signal = uOffset - signal; 
signal *= signal; 
 
float result = signal; 
float weight = 1.0; 
float frequency = 1.0; 
 
 
for(int i=0; i<uOctaves; i++){ 
 point *= uLacunarity; 
 weight = signal * uGain; 
 weight = clamp(weight, 0, 1); 
 signal = noise1(point); 
 signal = abs(signal); 
 signal *= weight; 
 result += signal * pow(frequency, -H); 
 frequency *= uLacunarity; 
 
} 
 
 
return result * uAmp; 
} 
 
 
void main() 
{ 
  
 vec3 p = uv.rgb; 
 float t = terrain(p); 
 vec4 color = vec4(vec3(t),1); 
 fragColor = color; 
}
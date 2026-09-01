using LinearAlgebra
a = [1.0, 2.0 ,3.0];
b = [4.0, 5.0, 6.0];

println(" a + b = ", a + b);
println(" a . b = ", dot(a,b));
println("|a|",sqrt(dot(a,b)) );
println("Cosine similarity", dot(a , b) / (sqrt(dot(a,a)) * sqrt(dot(b,b))));
# Matrix-vector multiplication
W = [0.1 -0.2 0.3; 0.4 0.5 -0.1]
x = [1.0, 0.5, -0.3]
println("wx = ", w * x)
println("This is a neural network layer.")
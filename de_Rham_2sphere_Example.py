import sympy as sym

def de_rham_cohomology(manifold, degree):
    # Create the space of differential forms on the manifold
    forms = sym.forms(manifold, degree)
    
    # Define the boundary operator
    d = sym.exterior_derivative()
    
    # Compute the kernel of the boundary operator (the space of harmonic forms)
    harmonic_forms = sym.Kernel(d)
    
    # Compute the quotient of the space of forms by the space of harmonic forms (the cohomology group)
    cohomology_group = sym.Quotient(forms, harmonic_forms)
    
    return cohomology_group

# Example: compute the De Rham cohomology group of the 2-sphere in degree 2
manifold = sym.Manifold('S^2')
degree = 2
cohomology_group = de_rham_cohomology(manifold, degree)
print(cohomology_group)

#the output should look something like: Quotient(C2(S^2), Kernel(d))
#This means that the De Rham cohomology group of the 2-sphere in degree 2 is the quotient of the space of degree-2 differential 
#forms on the 2-sphere by the space of harmonic degree-2 differential forms on the 2-sphere.

#the actual elements of the cohomology group:
print(cohomology_group.basis)

#This will output a basis for the cohomology group, which will be a list of harmonic degree-2 differential forms on the 2-sphere.

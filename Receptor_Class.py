class Receptor:
    """
    This class represents a receptor object with properties like
    name, location, and binding affinity.
    """

    def __init__(self, name, location, affinity):
        """
        Initialize a Receptor object with a name, location, and binding affinity.
        
        Args:
            name (str): The name of the receptor.
            location (str): The location of the receptor (e.g., cell membrane, nucleus).
            affinity (float): The binding affinity of the receptor (between 0 and 1).
        """
        self.name = name
        self.location = location
        self.affinity = affinity

    def bind_ligand(self, ligand_concentration):
        """
        Simulate the binding of a ligand to the receptor based on its concentration
        and the receptor's binding affinity.
        
        Args:
            ligand_concentration (float): The concentration of the ligand.
            
        Returns:
            bool: True if the ligand binds successfully, False otherwise.
        """
        if ligand_concentration * self.affinity > 0.5:
            return True
        else:
            return False

    def __str__(self):
        """
        Return a string representation of the Receptor object.
        """
        return f"Receptor: {self.name}, Location: {self.location}, Affinity: {self.affinity}"
    
 


# Create a Receptor object
receptor1 = Receptor("GPCR", "Cell Membrane", 0.8)

# Print the receptor object
print(receptor1)  # Output: Receptor: GPCR, Location: Cell Membrane, Affinity: 0.8

# Simulate ligand binding
ligand_concentration = 0.7
if receptor1.bind_ligand(ligand_concentration):
    print("Ligand bound successfully.")
else:
    print("Ligand binding failed.")

receptor1.statement()
from taxonomy_tree import Clade

def test_clade_creation():
    taxonomies = [
        ["Dinosauria", "Saurischia", "Theropoda"],
        ["Dinosauria", "Saurischia", "Sauropodomorpha"],
        ["Dinosauria", "Ornithischia", "Genasauria"]
    ]

    dinosauria = Clade.build(taxonomies)
    assert len(dinosauria.members) == 2
    assert "Ornithischia" in [clade.name for clade in dinosauria.members]
    ornithischia: Clade = [
        clade for clade in dinosauria.members 
        if clade.name == "Ornithischia"
    ][0]
    assert "Genasauria" in [clade.name for clade in ornithischia.members]


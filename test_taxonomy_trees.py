from taxonomy_tree import Clade

def test_clade():
    taxonomies = [
        ["Dinosauria", "Saurischia", "Theropoda"],
        ["Dinosauria", "Saurischia", "Sauropodomorpha"],
        ["Dinosauria", "Ornithischia", "Genasauria"]
    ]

    cladogram = Clade.build(taxonomies)
    assert len(cladogram.members) == 2
    assert cladogram.members[1].name == "Ornithischia"
    assert len(cladogram.members[1].members) == 1 

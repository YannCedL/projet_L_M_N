# Création de la classe infrastructure
class Infra:
    def __init__(self, infra_id, length,infra_type, nb_houses ) -> None:
        self.infra_id = infra_id
        self.length = length
        self.infra_type = infra_type
        self.nb_houses = nb_houses

    def repair_infra(self):
        self.infra_type = "infra_intacte"

    def 
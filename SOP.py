from docxtpl import DocxTemplate


class SOP:

    def __init__(self, navn, klasse, opgaveformulering, studieretningsfag, studieretningsvejleder, andetfag, andetfagvejleder):
        self.navn = navn
        self.klasse = klasse
        self.opgaveformulering = opgaveformulering
        self.studieretningsfag = studieretningsfag
        self.studieretningsvejleder = studieretningsvejleder
        self.andetfag = andetfag
        self.andetfagvejleder = andetfagvejleder

    def genererDocx(self):
        filnavn = self.navn + ".docx"
        doc = DocxTemplate('sop.docx')
        context = {
            'navn': self.navn,
            'klasse': self.klasse,
            'opgaveformulering': self.opgaveformulering,
            'studieretningsfag': self.studieretningsfag,
            'studieretningsvejleder': self.studieretningsvejleder,
            'andetfag': self.andetfag,
            'andetfagvejleder': self.andetfagvejleder,
        }
        doc.render(context)
        doc.save(filnavn)

    def udskriv(self):
        print("Navn:", self.navn)
        print("Klasse:", self.klasse)
        print("Opgaveformulering:", self.opgaveformulering)
        print("Studieretningsfag:", self.studieretningsfag)
        print("Studieretningsvejleder:", self.studieretningsvejleder)
        print("Andet fag", self.andetfag)
        print("Andet fag vejleder", self.andetfagvejleder)

from SOP import SOP


def læsFil(filnavn, SOPer):
    next = 0
    opgaveformulering = ""
    f = open(filnavn, "r")
    for linje in f:
        if linje[0] == "#" and linje[1] != "#" and next == 0:
            # ny SOP
            linje = linje.strip()
            linje = linje.split(",")
            navn = linje[0].strip('#').strip()
            klasse = linje[1].strip()
            next += 1
            print(navn, klasse)
        elif linje[0: 2] != "##":
            opgaveformulering += linje

        elif linje[0: 2] == "##" and next == 1:
            studieretningsfag = linje.strip('#').strip()
            next += 1

        elif linje[0: 2] == "##" and next == 2:
            studieretningsvejleder = linje.strip('#').strip()
            next += 1

        elif linje[0: 2] == "##" and next == 3:
            andetfag = linje.strip('#').strip()
            next += 1

        elif linje[0: 2] == "##" and next == 4:
            andetfagvejleder = linje.strip('#').strip()

            s = SOP(navn, klasse, opgaveformulering, studieretningsfag,
                    studieretningsvejleder, andetfag, andetfagvejleder)
            SOPer.append(s)

            opgaveformulering = ""
            next = 0


def main():
    SOPer = []
    print("Læser fil")
    læsFil("sop.md", SOPer)
    print("Filen er læst")
    print("Udskriver SOPer")
    print("Antal SOPer: ", len(SOPer))
    for s in SOPer:
        s.udskriv()
    # s.genererDocx()


main()
# generate_pdf("generated_doc.docx", "./")
# convert("generated_doc.docx", "generated_doc.pdf")

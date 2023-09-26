
SOPer = []


def læsFil(filnavn):
    SOP = None
    next = 'opgaveformulering'
    opgaveformulering = ""
    f = open(filnavn, "r")
    for linje in f:
        if linje[0] == "#" and linje[1] != "#":
            # ny SOP
            opgaveformulering = ""
            linje = linje.strip()
            linje = linje.split(",")
            navn = linje[0].strip('#').strip()
            klasse = linje[1].strip()
        elif linje[0: 2] != "##":
            opgaveformulering += linje
            next = 'studieretningsfag'
        elif linje[0: 2] == "##" and next == 'studieretningsfag':
            print(opgaveformulering)
            studieretningsfag = f.readline().strip()
            next = 'studieretningsvejleder'
        elif linje[0: 2] == "##" and next == 'studieretningsvejleder':
            studieretningsvejleder = f.readline().strip()
            next = 'andetfag'
        elif linje[0: 2] == "##" and next == 'andetfag':
            andetfag = f.readline().strip()
            next = 'andetfagvejleder'
        elif linje[0: 2] == "##" and next == 'andetfagvejleder':
            andetfagvejleder = f.readline().strip()
            next = 'opgaveformulering'
            SOP = SOP(navn, klasse, opgaveformulering, studieretningsfag,
                      studieretningsvejleder, andetfag, andetfagvejleder)
            SOPer.append(SOP)


læsFil("sop.md")
print("Antal SOPer:", len(SOPer))
for SOP in SOPer:
    # SOP.genererDocx()
    SOP.udskriv()


# generate_pdf("generated_doc.docx", "./")
# convert("generated_doc.docx", "generated_doc.pdf")
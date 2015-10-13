# Use Unicode Codepage UTF-8
# -*- coding: utf-8 -*-

# MODULE HEADER
#
# Module Name: "icpyqg.py"
#
# Module Description:
# This module contains functions used in QGIS scripts.
#
# Module Timeline:
# October 2015: Creation
#
# Author: Ioannis Dafermos
# Works in: QGIS
# Licensed under: EUPL V.1.1


# DEFINITIONS FOLLOW AFTER THIS LINE ------------------------------------------------------------------------------------------------------------------


# Function "convertGreekToLatinELOT743"
def convertGreekToLatinELOT743(theGreekString, theCodePage):
    """This function converts a Greek string to its Latin counterpart according to the ELOT-743 specifications.

    This function converts a Greek string to its Latin counterpart according to the ELOT-743 specifications.

    Return Value: This function returns a <String>, representing the Latin counterpart of the initial Greek string.

    Error Codes:   None

    Function Timeline:
    October 2015: Creation

    Author: Ioannis Dafermos
    Works in: QGIS
    Licensed under: EUPL V.1.1
    """

    # MAIN BODY OF FUNCTION -----------------------------------------------------------------------------------------------------

    # Initialize <theLatinString> and counter <i>
    theLatinString = ""
    i = 0
    
    # Loop through the characters of <theGreekString> in order to build <theLatinString>
    while i < len(theGreekString):
        # Get the character of <theGreekString> at position <i>
        theChar = theGreekString[i]

        # Unless <theChar> is a Greek character, it will remain unchanged.
        # Either way, it will be appended to <theLatinString> at the end of the loop.

        # Check for various Greek Characters
        if theChar == "Β".decode(theCodePage):
            theChar = "V"
        elif theChar == "β".decode(theCodePage):
            theChar = "v"
        elif theChar == "Δ".decode(theCodePage):
            theChar = "D"
        elif theChar == "δ".decode(theCodePage):
            theChar = "d"
        elif theChar == "Ζ".decode(theCodePage):
            theChar = "Z"
        elif theChar == "ζ".decode(theCodePage):
            theChar = "z"
        elif theChar == "θ".decode(theCodePage):
            theChar = "th"
        elif theChar == "Ι".decode(theCodePage):
            theChar = "I"
        elif theChar == "Ί".decode(theCodePage):
            theChar = "I"
        elif theChar == "Ϊ".decode(theCodePage):
            theChar = "I"
        elif theChar == "ι".decode(theCodePage):
            theChar = "i"
        elif theChar == "ί".decode(theCodePage):
            theChar = "i"
        elif theChar == "ϊ".decode(theCodePage):
            theChar = "i"
        elif theChar == "ΐ".decode(theCodePage):
            theChar = "i"
        elif theChar == "Κ".decode(theCodePage):
            theChar = "K"
        elif theChar == "κ".decode(theCodePage):
            theChar = "k"
        elif theChar == "Λ".decode(theCodePage):
            theChar = "L"
        elif theChar == "λ".decode(theCodePage):
            theChar = "l"
        elif theChar == "Ν".decode(theCodePage):
            theChar = "N"
        elif theChar == "ν".decode(theCodePage):
            theChar = "n"
        elif theChar == "Ξ".decode(theCodePage):
            theChar = "X"
        elif theChar == "ξ".decode(theCodePage):
            theChar = "x"
        elif theChar == "Π".decode(theCodePage):
            theChar = "P"
        elif theChar == "π".decode(theCodePage):
            theChar = "p"
        elif theChar == "Ρ".decode(theCodePage):
            theChar = "R"
        elif theChar == "ρ".decode(theCodePage):
            theChar = "r"
        elif theChar == "Σ".decode(theCodePage):
            theChar = "S"
        elif theChar == "σ".decode(theCodePage):
            theChar = "s"
        elif theChar == "ς".decode(theCodePage):
            theChar = "s"
        elif theChar == "Τ".decode(theCodePage):
            theChar = "T"
        elif theChar == "τ".decode(theCodePage):
            theChar = "t"
        elif theChar == "Υ".decode(theCodePage):
            theChar = "Y"
        elif theChar == "Ύ".decode(theCodePage):
            theChar = "Y"
        elif theChar == "Ϋ".decode(theCodePage):
            theChar = "Y"
        elif theChar == "υ".decode(theCodePage):
            theChar = "y"
        elif theChar == "ύ".decode(theCodePage):
            theChar = "y"
        elif theChar == "ϋ".decode(theCodePage):
            theChar = "y"
        elif theChar == "ΰ".decode(theCodePage):
            theChar = "y"
        elif theChar == "Φ".decode(theCodePage):
            theChar = "F"
        elif theChar == "φ".decode(theCodePage):
            theChar = "f"
        elif theChar == "χ".decode(theCodePage):
            theChar = "ch"
        elif theChar == "ψ".decode(theCodePage):
            theChar = "ps"
        elif theChar == "Ω".decode(theCodePage):
            theChar = "O"
        elif theChar == "Ώ".decode(theCodePage):
            theChar = "O"
        elif theChar == "ω".decode(theCodePage):
            theChar = "o"
        elif theChar == "ώ".decode(theCodePage):
            theChar = "o"

        # Check for Greek Character "Θ"
        if theChar == "Θ".decode(theCodePage):
            # Get <theNextChar> right after <Θ>
            theNextChar = theGreekString[i+1:i+2]

            # Check if <theNextChar> is a lower-case Greek character
            isNextCharLCase = isGreekLCase(theNextChar, theCodePage)

            # Do some error handling on the above
            if isNextCharLCase == -1:
                isNextCharLCase = False

            # Finally replace <theChar>
            if isNextCharLCase:
                theChar = "Th"
            else:
                theChar = "TH"

        # Check for Greek Character "Χ"
        if theChar == "Χ".decode(theCodePage):
            # Get <theNextChar> right after <Χ>
            theNextChar = theGreekString[i+1:i+2]

            # Check if <theNextChar> is a lower-case Greek character
            isNextCharLCase = isGreekLCase(theNextChar, theCodePage)

            # Do some error handling on the above
            if isNextCharLCase == -1:
                isNextCharLCase = False

            # Finally replace <theChar>
            if isNextCharLCase:
                theChar="Ch"
            else:
                theChar="CH"

        # Check for Greek Character "Ψ"
        if theChar == "Ψ".decode(theCodePage):
            # Get <theNextChar> right after <Ψ>
            theNextChar = theGreekString[i+1:i+2]

            # Check if <theNextChar> is a lower-case Greek character
            isNextCharLCase = isGreekLCase(theNextChar, theCodePage)

            # Do some error handling on the above
            if isNextCharLCase == -1:
                IsNextCharLCase = False

            # Finally replace <theChar>
            if isNextCharLCase:
                theChar="Ps"
            else:
                theChar="PS"

        # Check for Greek Character "Α"
        if theChar == "Α".decode(theCodePage):
            # Get <thePair> of the two consecutive characters of <theGreekString>
            thePair = theGreekString[i:i+2]

            # Get <theNextChar> right after <Α>
            theNextChar = theGreekString[i+1:i+2]

            if thePair == "ΑΥ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "AV"
                else:
                    i = i + 1
                    theChar = "AF"
            elif thePair == "Αυ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "Av"
                else:
                    i = i + 1
                    theChar = "Af"
            elif thePair == "Αύ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "Av"
                else:
                    i = i + 1
                    theChar = "Af"
            else:
                theChar = "A"

        # Check for Greek Character "Ά"
        if theChar == "Ά".decode(theCodePage):
            theChar="A"

        # Check for Greek Character "α"
        if theChar == "α".decode(theCodePage):
            # Get <thePair> of the two consecutive characters of <theGreekString>
            thePair = theGreekString[i:i+2]

            # Get <theNextChar> right after <α>
            theNextChar = theGreekString[i+1:i+2]

            if thePair == "αΥ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)
                    
                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "aV"
                else:
                    i = i + 1
                    theChar = "aF"
            elif thePair == "αυ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)
                    
                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "av"
                else:
                    i = i + 1
                    theChar = "af"
            elif thePair == "αύ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)
                    
                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "av"
                else:
                    i = i + 1
                    theChar = "af"
            else:
                theChar = "a"

        # Check for Greek Character "ά"
        if theChar == "ά".decode(theCodePage):
            theChar="a"

        # Check for Greek Character "Γ"
        if theChar == "Γ".decode(theCodePage):
            # Get <thePair> of the two consecutive characters of <theGreekString>
            thePair = theGreekString[i:i+2]

            if thePair == "ΓΓ".decode(theCodePage):
                i = i + 1
                theChar = "NG"
            elif thePair == "Γγ".decode(theCodePage):
                i = i + 1
                theChar = "Ng"
            elif thePair == "ΓΞ".decode(theCodePage):
                i = i + 1
                theChar = "NX"
            elif thePair == "Γξ".decode(theCodePage):
                i = i + 1
                theChar = "Nx"
            elif thePair == "ΓΧ".decode(theCodePage):
                i = i + 1
                theChar = "NCH"
            elif thePair == "Γχ".decode(theCodePage):
                i = i + 1
                theChar = "Nch"
            else:
                theChar="G"   		      

        # Check for Greek Character "γ"
        if theChar == "γ".decode(theCodePage):
            # Get <thePair> of the two consecutive characters of <theGreekString>
            thePair = theGreekString[i:i+2]

            if thePair == "γΓ".decode(theCodePage):
                i = i + 1
                theChar = "nG"
            elif thePair == "γγ".decode(theCodePage):
                i = i + 1
                theChar = "ng"
            elif thePair == "γΞ".decode(theCodePage):
                i = i + 1
                theChar = "nX"
            elif thePair == "γξ".decode(theCodePage):
                i = i + 1
                theChar = "nx"
            elif thePair == "γΧ".decode(theCodePage):
                i = i + 1
                theChar = "nCH"
            elif thePair == "γχ".decode(theCodePage):
                i = i + 1
                theChar = "nch"
            else:
                theChar = "g"   		      

        # Check for Greek Character "Ε"
        if theChar == "Ε".decode(theCodePage):
            # Get <thePair> of the two consecutive characters of <theGreekString>
            thePair = theGreekString[i:i+2]

            # Get <theNextChar> right after <Ε>
            theNextChar = theGreekString[i+1:i+2]

            if thePair == "ΕΥ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "EV"
                else:
                    i = i + 1
                    theChar = "EF"
            elif thePair == "Ευ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "Ev"
                else:
                    i = i + 1
                    theChar = "Ef"
            elif thePair == "Εύ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "Ev"
                else:
                    i = i + 1
                    theChar = "Ef"
            else:
                theChar="E"      

        # Check for Greek Character "Έ"
        if theChar == "Έ".decode(theCodePage):
            theChar="E"

        # Check for Greek Character "ε"
        if theChar == "ε".decode(theCodePage):
            # Get <thePair> of the two consecutive characters of <theGreekString>
            thePair = theGreekString[i:i+2]

            # Get <theNextChar> right after <ε>
            theNextChar = theGreekString[i+1:i+2]

            if thePair == "εΥ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "eV"
                else:
                    i = i + 1
                    theChar = "eF"
            elif thePair == "ευ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)
                    
                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "ev"
                else:
                    i = i + 1
                    theChar = "ef"
            elif thePair == "εύ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "ev"
                else:
                    i = i + 1
                    theChar = "ef"
            else:
                theChar="e"

        # Check for Greek Character "έ"
        if theChar == "έ".decode(theCodePage):
            theChar="e"

        # Check for Greek Character "Η"
        if theChar == "Η".decode(theCodePage):
            # Get <thePair> of the two consecutive characters of <theGreekString>
            thePair = theGreekString[i:i+2]

            # Get <theNextChar> right after <Η>
            theNextChar = theGreekString[i+1:i+2]

            if thePair == "ΗΥ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                IsContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "ΙV"
                else:
                    i = i + 1
                    theChar = "ΙF"
            elif thePair == "Ηυ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "Ιv"
                else:
                    i = i + 1
                    theChar = "Ιf"
            elif thePair == "Ηύ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)
                    
                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "Ιv"
                else:
                    i = i + 1
                    theChar = "Ιf"
            else:
                theChar = "I"

        # Check for Greek Character "Ή"
        if theChar == "Ή".decode(theCodePage):
            theChar="I"

        # Check for Greek Character "η"
        if theChar == "η".decode(theCodePage):
            # Get <thePair> of the two consecutive characters of <theGreekString>
            thePair = theGreekString[i:i+2]

            # Get <theNextChar> right after <η>
            theNextChar = theGreekString[i+1:i+2]

            if thePair == "ηΥ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "iV"
                else:
                    i = i + 1
                    theChar = "iF"
            elif thePair == "ηυ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "iv"
                else:
                    i = i + 1
                    theChar = "if"
            elif thePair == "ηύ".decode(theCodePage):
                # Get <theThirdChar> right after <thePair>
                theThirdChar = theGreekString[i+2:i+3]

                # Check if <theThirdChar> is contained in the set of characters "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ"
                theCSet = "ΒΓΔΖΛΜΝΡΕΟΗΩΑΙΥβγδζλμνρεοηωαιυ".decode(theCodePage)
                isContained = theThirdChar in theCSet

                # If <isContained> remains <False>, then check if <theThirdChar> is contained in this set of special characters:
                # [Ά,ά,Έ,έ,Ή,ή,Ί,Ϊ,ί,ϊ,ΐ,Ό,ό,Ύ,Ϋ,ύ,ϋ,ΰ,Ώ,ώ]
                if isContained == False:
                    theSpecialCharacters = "ΆάΈέΉήΊΪίϊΐΌόΎΫύϋΰΏώ".decode(theCodePage)

                    # If <theThirdChar> is contained in <theSpecialCharacters>, then set <isContained> to <True>
                    if theThirdChar in theSpecialCharacters:
                        isContained = True

                # Act according to the value of <isContained>
                if isContained:
                    i = i + 1
                    theChar = "iv"
                else:
                    i = i + 1
                    theChar = "if"
            else:
                theChar = "i"

        # Check for Greek Character "ή"
        if theChar == "ή".decode(theCodePage):
            theChar="i"

        # Check for Greek Character "Μ"
        if theChar == "Μ".decode(theCodePage):
            # Get <thePair> of the two consecutive characters of <theGreekString>
            thePair = theGreekString[i:i+2]

            if thePair == "ΜΠ".decode(theCodePage):
                if i == 0:
                    # If "ΜΠ" is at the beginning of <theGreekString> then replace it with "B"
                    i = i + 1
                    theChar = "B"
                elif i == (len(theGreekString) - 2):
                    # If "ΜΠ" is at the end of <theGreekString> then replace it with "B"
                    i = i + 1
                    theChar = "B"
                elif theGreekString[i:i+3] == "ΜΠ ".decode(theCodePage):
                    i = i + 1
                    theChar = "B"
                elif theGreekString[i-1:i+2] == " ΜΠ".decode(theCodePage):
                    i = i + 1
                    theChar = "B"
                else:
                    i = i + 1
                    theChar = "MP"
            elif thePair == "Μπ".decode(theCodePage):
                if i == 0:
                    # If "Μπ" is at the beginning of <theGreekString> then replace it with "B"
                    i = i + 1
                    theChar = "B"
                elif i == (len(theGreekString) - 2):
                    # If "Μπ" is at the end of <theGreekString> then replace it with "B"
                    i = i + 1
                    theChar = "B"
                elif theGreekString[i:i+3] == "Μπ ".decode(theCodePage):
                    i = i + 1
                    theChar = "B"
                elif theGreekString[i-1:i+2] == " Μπ".decode(theCodePage):
                    i = i + 1
                    theChar = "B"
                else:
                    i = i + 1
                    theChar = "Mp"
            else:
                theChar = "M"

        # Check for Greek Character "μ"
        if theChar == "μ".decode(theCodePage):
            # Get <thePair> of the two consecutive characters of <theGreekString>
            thePair = theGreekString[i:i+2]

            if thePair == "μΠ".decode(theCodePage):
                if i == 0:
                    # If "μΠ" is at the beginning of <theGreekString> then replace it with "b"
                    i = i + 1
                    theChar = "b"
                elif i == (len(theGreekString) - 2):
                    # If "μΠ" is at the end of <theGreekString> then replace it with "b"
                    i = i + 1
                    theChar = "b"
                elif theGreekString[i:i+3] == "μΠ ".decode(theCodePage):
                    i = i + 1
                    theChar = "b"
                elif theGreekString[i-1:i+2] == " μΠ".decode(theCodePage):
                    i = i + 1
                    theChar = "b"
                else:
                    i = i + 1
                    theChar = "mP"
            elif thePair == "μπ".decode(theCodePage):
                if i == 0:
                    # If "μπ" is at the beginning of <theGreekString> then replace it with "b"
                    i = i + 1
                    theChar = "b"
                elif i == (len(theGreekString) - 2):
                    # If "μπ" is at the end of <theGreekString> then replace it with "b"
                    i = i + 1
                    theChar = "b"
                elif theGreekString[i:i+3] == "μπ ".decode(theCodePage):
                    i = i + 1
                    theChar = "b"
                elif theGreekString[i-1:i+2] == " μπ".decode(theCodePage):
                    i = i + 1
                    theChar = "b"
                else:
                    i = i + 1
                    theChar = "mp"
            else:
                theChar = "m"

        # Check for Greek Character "Ο"
        if theChar == "Ο".decode(theCodePage):
            # Get <thePair> of the two consecutive characters of <theGreekString>
            thePair = theGreekString[i:i+2]

            # Get <theNextChar> right after <Ο>
            theNextChar = theGreekString[i+1:i+2]

            if thePair == "ΟΥ".decode(theCodePage):
                i = i + 1
                theChar = "OU"
            elif thePair == "Ου".decode(theCodePage):
                i = i + 1
                theChar = "Ou"
            elif thePair == "Ού".decode(theCodePage):
                i = i + 1
                theChar = "Ou"
            else:
                theChar="O"
                
        # Check for Greek Character "Ό"
        if theChar == "Ό".decode(theCodePage):
            theChar="O"

        # Check for Greek Character "ο"
        if theChar == "ο".decode(theCodePage):
            # Get <thePair> of the two consecutive characters of <theGreekString>
            thePair = theGreekString[i:i+2]

            # Get <theNextChar> right after <ο>
            theNextChar = theGreekString[i+1:i+2]

            if thePair == "οΥ".decode(theCodePage):
                i = i + 1
                theChar = "oU"
            elif thePair == "ου".decode(theCodePage):
                i = i + 1
                theChar = "ou"
            elif thePair == "ού".decode(theCodePage):
                i = i + 1
                theChar = "ou"
            else:
                theChar = "o"

        # Check for Greek Character "ό"
        if theChar == "ό".decode(theCodePage):
            theChar="o"

        # END OF FUNCTION MAIN BODY --------------------------------------------------------------------------------------------------------

        # Append <theChar> to <theLatinString>
        theLatinString = theLatinString + theChar

        # Increment <i> by one
        i = i + 1

    # Return a value to the caller. <Return> without an expression argument returns <None>.
    # Falling off the end of a function without an explicit return statement also returns <None>.
    return theLatinString


# -----------------------------------------------------------------------------------------------------------------------------------------------------


# Function "isGreekLCase"
def isGreekLCase(theChar, theCodePage):
    """This function checks whether character <theChar> is a lower-case Greek character or not.

    This function checks whether character <theChar> is a lower-case Greek character or not.
    Object <theChar> must be a single character (a string of one element).
    
    Return Value: This function returns <True> or <False> depending on whether <theChar> is a lower-case Greek character or not.

    Error Codes:   -1 = <theChar> contains other than one (1) characters

    Function Timeline:
    October 2015: Creation

    Author: Ioannis Dafermos
    Works in: QGIS
    Licensed under: EUPL V.1.1
    """

    # If <theChar> is <None>, then return <False>
    if theChar is None:
        return False

    # If <theChar> is " ", then return <False>
    if theChar == " ".decode(theCodePage):
        return False

    # Check if <theChar> contains other than one (1) characters
    if len(theChar) <> 1:
        return -1

    # MAIN BODY OF FUNCTION -----------------------------------------------------------------------------------------------------

    # Make <theGreekLCaseChars> string
    theGreekLCaseChars = "αάβγδεέζηήθιίϊΐκλμνξοόπρσςτυύϋΰφχψωώ".decode(theCodePage)

    # Initialize <theCharIsLCase> by assuming that it is <False>
    theCharIsLCase = False

    # If <theChar> is contained in <theGreekLCaseChars> then set <theCharIsLCase> to <True>
    if theChar in theGreekLCaseChars:
        theCharIsLCase = True

    # Return <theCharIsLCase>
    return theCharIsLCase

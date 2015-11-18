### Επεξεργασία δεδομένων του OpenStreetMap Project για χρήση από εφαρμογές GIS - Μέρος Α’
**Πιλοτική Εφαρμογή στην Περιφέρεια Αττικής (πλην Νήσων) _(OSM-Street-Network-Corrections-Attica)_**

Το OpenStreetMap Project παρέχει δεδομένα οδικού δικτύου με εκτενή γεωγραφική κάλυψη που μπορούν να εξυπηρετήσουν πολλαπλές ανάγκες. Η λεπτομέρεια των δεδομένων καθώς και η διαρκής ενημέρωσή τους από μία ευρεία κοινότητα χρηστών παρέχουν ένα πολύ καλό υπόβαθρο για εφαρμογές που σχετίζονται με οδικά συγκοινωνιακά δίκτυα.

Ωστόσο, στην πρωτογενή τους μορφή τα δεδομένα αυτά δεν μπορούν να χρησιμοποιηθούν άμεσα από αρκετές εφαρμογές GIS, όπως εφαρμογές πλοήγησης, εύρεσης βέλτιστης διαδρομής κλπ., λόγω ορισμένων αδυναμιών που παρουσιάζουν, όπως:

1. Μη ύπαρξη τοπολογικών κόμβων (nodes) στις περισσότερες διασταυρώσεις των αξόνων.
2. Ατέλειες και ασυνέχειες της κατηγοριοποίησης των οδικών αξόνων.

Στόχος του παρόντος έργου είναι η αντιμετώπιση των προβλημάτων αυτών, ώστε να καταστεί το οδικό δίκτυο του OSM περισσότερο αξιοποιήσιμο από εφαρμογές GIS, κάνοντας τη λιγότερη δυνατή χειρωνακτική εργασία. Για τον λόγο αυτό καταρτίστηκε εξειδικευμένη μεθοδολογία, υποβοηθούμενη από customization scripts, μέσα στο περιβάλλον του ελεύθερου open-source λογισμικού QGIS και εφαρμόστηκε πιλοτικά στην Περιφέρεια Αττικής.

Υπάρχουν πολλά ακόμη που μπορούν να γίνουν ώστε να καταστεί ένα οδικό δίκτυο ακόμη πιο αξιοποιήσιμο από εφαρμογές GIS (όπως λεπτομερέστερη κατηγοριοποίηση των τόξων του δικτύου, εισαγωγή ειδικών περιορισμών κίνησης, τυποποίηση αναγραφών ονομασιών οδών κ.α.), εντούτοις σκοπός του παρόντος έργου είναι η αντιμετώπιση των δύο κυριότερων αδυναμιών που προαναφέρθηκαν.

Για περισσότερες πληροφορίες, παρακαλώ δείτε το [Wiki Page](https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/wiki).

Τεκμηρίωση για τη διαδικασία παρέχεται στα pdf αρχεία:
* **Διαδικασία_Διορθώσεων_OSM_QGIS.pdf**: Πλήρης καταγραφή διαδικασίας & εργασιών για developers και χρήστες που ενδιαφέρονται να την εφαρμόσουν, τροποποιήσουν, επεκτείνουν κλπ.
* **Διαδικασία_Διορθώσεων_OSM_Simple.pdf**: Συνοπτικές οδηγίες για απλούς χρήστες.

Τα παραπάνω αρχεία βρίσκονται στο archive: [_OSM_Street_Network_Corrections_Reports.7z_](https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/blob/master/OSM_Street_Network_Corrections_Reports.7z)

Μπορείτε να καταχωρείτε ως [issues](https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/issues) όποιες βελτιώσεις, δυσλειτουργίες, προτάσεις κλπ. έχετε εντοπίσει σχετικά με το έργο αυτό.

Δείτε επίσης το έργο "Επεξεργασία δεδομένων του OpenStreetMap Project για χρήση από εφαρμογές GIS - Μέρος Β’: Επέκταση στην υπόλοιπη Ελλάδα ([OSM-Street-Network-Corrections-Greece](https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Greece))", το οποίο αποτελεί επέκταση εφαρμογής του παρόντος.

**Παραδοτέα**

Τα παραδοτέα αρχεία του έργου βρίσκονται στους εξής συνδέσμους:

|       |                          **Παραδοτέο**                            |**URL**|
|:-----:|:------------------------------------------------------------------|:-----:|
|   1   |Καταγραφή διαδικασιών|https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/blob/master/OSM_Street_Network_Corrections_Reports.7z|
|   2   |Scripts παραμετροποίησης|https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/blob/master/Script_Convert_Greek_to_Latin_ELOT743.7z|
|   3   |Shapefile Αττικής σε WGS'84|https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/blob/master/roads_corrected_wgs84_attiki.7z|
|   4   |Shapefile Αττικής σε ΕΓΣΑ'87|https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/blob/master/roads_corrected_ggrs87_attiki.7z|

Μπορείτε να [κατεβάσετε και από Dropbox τα παραδοτέα αρχεία](https://www.dropbox.com/sh/gnx81f1zytrbfdq/AACqHRXdpPdOy_GUzlT91JXGa?dl=0) του έργου. _Ορισμένα αρχεία λόγω του μεγέθους τους δεν στάθηκε δυνατόν να ανέβουν στο αποθετήριο του έργου._

Δείτε εδώ αναλυτικότερες [πληροφορίες για τα Παραδοτέα](https://github.com/ellak-monades-aristeias/OSM-Street-Network-Corrections-Attica/wiki/Deliverables).

**Το υλικό του έργου αυτού διατίθεται υπό τις Άδειες:**
- CC-BY-SA 4.0: Αρχεία διαδικασιών, πινάκων, κειμένων κλπ.
- EUPL 1.1: Scripts παραμετροποίησης
- ODbL 1.0: Χαρτογραφικά δεδομένα (shapefiles) από OSM (πρωτογενή αρχεία) & διορθωμένα παράγωγα αυτών


## Σε ποίους απευθύνεται - Κοινότητες Χρηστών - Προγραμματιστών(Developers) ##
...εδώ περιγράφετε τους δυνητικούς τελικούς χρήστες του έργου σας και τις κοινότητες χρηστών/developers που θα ενδιαφερόντουσαν να επεκτείνουν το έργο σας. ...

 

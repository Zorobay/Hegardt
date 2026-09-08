package se.hegardt.domain

import groovy.transform.CompileStatic
import groovy.transform.EqualsAndHashCode
import jakarta.persistence.Column
import jakarta.persistence.Entity
import jakarta.persistence.FetchType
import jakarta.persistence.GeneratedValue
import jakarta.persistence.GenerationType
import jakarta.persistence.Id
import jakarta.persistence.JoinColumn
import jakarta.persistence.ManyToOne
import jakarta.persistence.SequenceGenerator

@Entity
@CompileStatic
@EqualsAndHashCode(includes = ['id'])
class PdfReference {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = 'pdf_reference_seq')
    @SequenceGenerator(name = 'pdf_reference_seq', sequenceName = 'pdf_reference_seq', allocationSize = 1)
    Long id

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "person_id", nullable = false)
    Person person

    @Column(name = "pdf_page", nullable = false)
    Integer pdfPage

    @Column(nullable = false)
    Double x0

    @Column(nullable = false)
    Double y0

    @Column(nullable = false)
    Double x1

    @Column(nullable = false)
    Double y1

}

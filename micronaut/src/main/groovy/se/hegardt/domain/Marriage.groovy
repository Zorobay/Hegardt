package se.hegardt.domain

import groovy.transform.CompileStatic
import groovy.transform.EqualsAndHashCode
import jakarta.annotation.Nullable
import jakarta.persistence.*
import se.hegardt.domain.abstr.BaseEntity

@Entity
@CompileStatic
@EqualsAndHashCode(includes = ['id'])
class Marriage extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "marriage_seq")
    @SequenceGenerator(name = "marriage_seq", sequenceName = "marriage_seq", allocationSize = 1)
    Long id

    String notes

    @ManyToOne
    @JoinColumn(name = "spouse_1_id")
    Person spouse1

    @ManyToOne
    @JoinColumn(name = "spouse_2_id")
    Person spouse2

    @Embedded
    PartialDate date = new PartialDate()

    @ManyToOne(cascade = CascadeType.ALL)
    @Nullable
    Location location

    @PrePersist
    @PreUpdate
    void computeDates() {
        date?.computeDate()
    }
}

package se.hegardt.domain

import groovy.transform.CompileStatic
import io.micronaut.core.annotation.Nullable
import jakarta.persistence.*
import se.hegardt.domain.abstr.BaseEntity
import se.hegardt.model.Sex

@Entity
@CompileStatic
class Person extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "person_seq")
    @SequenceGenerator(name = "person_seq", sequenceName = "person_seq", allocationSize = 1)
    Long id

    String firstName
    String lastName
    String middleNames

    String notes

    @Enumerated(EnumType.STRING)
    Sex sex

    @Nullable
    Integer pdfPage

    @ManyToOne
    @Nullable
    Person father

    @ManyToOne
    @Nullable
    Person mother

    @OneToOne(cascade = CascadeType.ALL, orphanRemoval = true)
    @Nullable
    LifeEvent birth

    @OneToOne(cascade = CascadeType.ALL, orphanRemoval = true)
    @Nullable
    LifeEvent death

    @OneToOne(cascade = CascadeType.ALL, orphanRemoval = true)
    @Nullable
    LifeEvent burial

    @OneToMany(cascade = CascadeType.ALL, orphanRemoval = true)
    @JoinTable(
        name = "person_occupations",
        joinColumns = @JoinColumn(name = "person_id"),
        inverseJoinColumns = @JoinColumn(name = "occupation_id")
    )
    List<Occupation> occupations = []
}

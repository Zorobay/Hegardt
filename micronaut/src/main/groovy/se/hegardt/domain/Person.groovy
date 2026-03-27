package se.hegardt.domain

import groovy.transform.CompileStatic
import groovy.transform.EqualsAndHashCode
import io.micronaut.core.annotation.Nullable
import jakarta.persistence.*
import se.hegardt.domain.abstr.BaseEntity
import se.hegardt.helper.StringHelper
import se.hegardt.model.Sex

@Entity
@CompileStatic
@EqualsAndHashCode(includes = ['id'])
class Person extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "person_seq")
    @SequenceGenerator(name = "person_seq", sequenceName = "person_seq", allocationSize = 1)
    Long id

    String firstName
    String lastName
    String middleNames
    String normalizedName

    String notes

    @Enumerated(EnumType.STRING)
    Sex sex

    @Nullable
    Integer pdfPage

    @ManyToOne(fetch = FetchType.LAZY)
    @Nullable
    Person father

    @ManyToOne(fetch = FetchType.LAZY)
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

    @PrePersist
    @PreUpdate
    void computeNormalizedName() {
        normalizedName = StringHelper.normalize(fullName())
    }

    String fullName() {
        return [firstName, middleNames, lastName].grep().join(' ')
    }
}

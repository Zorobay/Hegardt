package se.hegardt.domain

import groovy.transform.CompileStatic
import groovy.transform.EqualsAndHashCode
import io.micronaut.core.annotation.Nullable
import jakarta.persistence.CascadeType
import jakarta.persistence.Entity
import jakarta.persistence.EnumType
import jakarta.persistence.Enumerated
import jakarta.persistence.FetchType
import jakarta.persistence.GeneratedValue
import jakarta.persistence.GenerationType
import jakarta.persistence.Id
import jakarta.persistence.JoinColumn
import jakarta.persistence.JoinTable
import jakarta.persistence.ManyToOne
import jakarta.persistence.OneToMany
import jakarta.persistence.OneToOne
import jakarta.persistence.PrePersist
import jakarta.persistence.PreUpdate
import jakarta.persistence.SequenceGenerator
import se.hegardt.domain.abstr.BaseEntity
import se.hegardt.helper.StringHelper
import se.hegardt.model.Sex

@Entity
@CompileStatic
@EqualsAndHashCode(includes = ['id'])
class Person extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = 'person_seq')
    @SequenceGenerator(name = 'person_seq', sequenceName = 'person_seq', allocationSize = 1)
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
        name = 'person_occupations',
        joinColumns = @JoinColumn(name = 'person_id'),
        inverseJoinColumns = @JoinColumn(name = 'occupation_id')
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

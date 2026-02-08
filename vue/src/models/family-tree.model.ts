import { Coordinates } from '@/models/coordinates.model.ts';
import { v4 as uuidv4 } from 'uuid';
import type { Sex } from '@/enums/PersonSexEnum.ts';
import type { Person, PersonsData } from '@/types/person.type.ts';
import { formatPersonFullName, formatPersonLifespan } from '@/helpers/person-helper.ts';

export class Connection {
  startCoordinates: Coordinates;
  endCoordinates: Coordinates;
  id: string = uuidv4();
  constructor(startCoordinates: Coordinates, endCoordinates: Coordinates) {
    this.startCoordinates = startCoordinates;
    this.endCoordinates = endCoordinates;
  }

  getCenter(): Coordinates {
    return new Coordinates(
      this.startCoordinates.x + (this.endCoordinates.x - this.startCoordinates.x) / 2,
      this.startCoordinates.y + (this.endCoordinates.y - this.startCoordinates.y) / 2,
    );
  }
}

export class FamilyTreeNode {
  x: number = 0;
  y: number = 0;
  id: number;
  fullName: string;
  sex: Sex;
  lifespan: string;
  father?: FamilyTreeNode;
  mother?: FamilyTreeNode;

  cardWidth: number = 0;
  cardHeight: number = 0;

  constructor(person: Person, cardWidth: number, cardHeight: number) {
    this.fullName = formatPersonFullName(person);
    this.id = person.id;
    this.sex = person.sex;
    this.lifespan = formatPersonLifespan(person);
    this.cardWidth = cardWidth;
    this.cardHeight = cardHeight;
  }

  getMaxAntecedentDepth(): number {
    return this.getMaxAntecedentDepthRec() - 1;
  }

  getRightCenterCoordinates(): Coordinates {
    return new Coordinates(this.x + this.cardWidth, this.y + this.cardHeight / 2);
  }

  getLeftCenterCoordinates(): Coordinates {
    return new Coordinates(this.x, this.y + this.cardHeight / 2);
  }

  getTopCenterCoordinates(): Coordinates {
    return new Coordinates(this.x + this.cardWidth / 2, this.y);
  }

  getCenterCoordinates(): Coordinates {
    return new Coordinates(this.x + this.cardWidth / 2, this.y + this.cardHeight / 2);
  }

  private getMaxAntecedentDepthRec(): number {
    const paternalAntecedentDepth = this.father?.getMaxAntecedentDepth() ?? 0;
    const maternalAntecedentDepth = this.mother?.getMaxAntecedentDepth() ?? 0;
    return 1 + Math.max(paternalAntecedentDepth, maternalAntecedentDepth);
  }
}

export class FamilyTreeConfig {
  personCardWidth: number = 200;
  personCardHeight: number = 68;
  horizontalSpacing: number = 80;
  verticalSpacing: number = 20;
  originCoordinates: Coordinates = new Coordinates(0, 0);
}

export class FamilyTree {
  rootNode: FamilyTreeNode | null = null;
  config: FamilyTreeConfig = new FamilyTreeConfig();
  treeDepth: number = 0;
  maxRenderDepth: number = 3;
  maxTreeBuildDepth: number = 50;
  straightConnections: Connection[] = [];
  parentChildConnections: Connection[] = [];

  constructor(config: FamilyTreeConfig = new FamilyTreeConfig()) {
    this.config = config;
  }

  getCenterCoordinates(): Coordinates {
    if (!this.rootNode) {
      return new Coordinates();
    }
    return this.rootNode.getCenterCoordinates();
  }

  getNodesToRender(): FamilyTreeNode[] {
    if (!this.rootNode) {
      return [];
    }

    const allNodes: FamilyTreeNode[] = [];
    this.selectNodesToRender(this.rootNode, allNodes, 0);
    return allNodes;
  }

  rebuild(rootPersonId: number, rawPersonsData: PersonsData): void {
    this.rootNode = this.buildNode(rootPersonId, rawPersonsData, 0);
    this.calculateCoordinates();
    this.buildConnections();
  }

  setMaxRenderDepth(maxRenderDepth: number): void {
    this.maxRenderDepth = maxRenderDepth;
    this.calculateCoordinates();
    this.buildConnections();
  }

  calculateCoordinates(): void {
    console.log('Recalculating coordinates');
    if (!this.rootNode) {
      return;
    }
    this.rootNode.x = this.config.originCoordinates.x;
    this.rootNode.y = this.config.originCoordinates.y;
    const depth = 0;
    const fatherNode = this.rootNode.father;
    if (fatherNode) {
      fatherNode.x = this.rootNode.x - (this.config.personCardWidth / 2 + this.config.horizontalSpacing);
      fatherNode.y = this.rootNode.y - (this.config.personCardHeight + this.config.verticalSpacing);
      this.calculateParentCoordinates(fatherNode, depth + 1, 1);
    }
    const motherNode = this.rootNode.mother;
    if (motherNode) {
      motherNode.x = this.rootNode.x + (this.config.personCardWidth / 2 + this.config.horizontalSpacing);
      motherNode.y = this.rootNode.y - (this.config.personCardHeight + this.config.verticalSpacing);
      this.calculateParentCoordinates(motherNode, depth + 1, -1);
    }
  }

  buildConnections(): void {
    if (!this.rootNode) {
      return;
    }
    this.straightConnections = [];
    this.parentChildConnections = [];
    const depth = 1;
    const father = this.rootNode.father;
    const mother = this.rootNode.mother;

    if (father && mother) {
      const connectionParentToParent = new Connection(
        father.getRightCenterCoordinates(),
        mother.getLeftCenterCoordinates(),
      );
      const connectionParentsToChild = new Connection(
        connectionParentToParent.getCenter(),
        this.rootNode.getTopCenterCoordinates(),
      );
      this.straightConnections.push(connectionParentToParent, connectionParentsToChild);
    }
    if (father) {
      this.buildPatriarchalConnections(father, depth);
    }
    if (mother) {
      this.buildMatriarchalConnections(mother, depth);
    }
  }

  private calculateParentCoordinates(node: FamilyTreeNode, depth: number, horizontalShiftMultiplier: number): void {
    if (depth >= this.maxRenderDepth) {
      return;
    }
    const exp = this.maxRenderDepth - depth - 1;
    const verticalMultiplier = Math.pow(2, exp);

    const fatherNode = node.father;
    if (fatherNode) {
      fatherNode.x = node.x - (this.config.personCardWidth + this.config.horizontalSpacing) * horizontalShiftMultiplier;
      fatherNode.y = node.y + (this.config.personCardHeight / 2 + this.config.verticalSpacing) * verticalMultiplier;
      this.calculateParentCoordinates(fatherNode, depth + 1, horizontalShiftMultiplier);
    }
    const motherNode = node.mother;
    if (motherNode) {
      motherNode.x = node.x - (this.config.personCardWidth + this.config.horizontalSpacing) * horizontalShiftMultiplier;
      motherNode.y = node.y - (this.config.personCardHeight / 2 + this.config.verticalSpacing) * verticalMultiplier;
      this.calculateParentCoordinates(motherNode, depth + 1, horizontalShiftMultiplier);
    }
  }

  private selectNodesToRender(node: FamilyTreeNode, selectedNodes: FamilyTreeNode[], depth: number): void {
    if (depth > this.maxRenderDepth) {
      return;
    }

    selectedNodes.push(node);

    if (node.father) {
      this.selectNodesToRender(node.father, selectedNodes, depth + 1);
    }
    if (node.mother) {
      this.selectNodesToRender(node.mother, selectedNodes, depth + 1);
    }
  }

  private buildNode(personId: number, rawPersonsData: PersonsData, depth: number): FamilyTreeNode {
    this.treeDepth = Math.max(this.treeDepth, depth);
    const person = rawPersonsData[personId];
    const node = new FamilyTreeNode(person, this.config.personCardWidth, this.config.personCardHeight);
    if (depth > this.maxTreeBuildDepth) {
      return node;
    }

    node.father = person.father ? this.buildNode(person.father, rawPersonsData, depth + 1) : undefined;
    node.mother = person.mother ? this.buildNode(person.mother, rawPersonsData, depth + 1) : undefined;
    return node;
  }

  private buildPatriarchalConnections(node: FamilyTreeNode, depth: number): void {
    if (depth >= this.maxRenderDepth) {
      return;
    }
    const father = node.father;
    const mother = node.mother;
    [father, mother]
      .filter((parent) => parent != null)
      .forEach((parent) => {
        this.parentChildConnections.push(this.getPatriarchalConnection(node, parent));
        this.buildPatriarchalConnections(parent, depth + 1);
      });
  }

  private buildMatriarchalConnections(node: FamilyTreeNode, depth: number): void {
    if (depth >= this.maxRenderDepth) {
      return;
    }
    const father = node.father;
    const mother = node.mother;
    [father, mother]
      .filter((parent) => parent != null)
      .forEach((parent) => {
        this.parentChildConnections.push(this.getMatriarchalConnection(node, parent));
        this.buildMatriarchalConnections(parent, depth + 1);
      });
  }

  private getPatriarchalConnection(rootNode: FamilyTreeNode, parent: FamilyTreeNode): Connection {
    return new Connection(parent.getRightCenterCoordinates(), rootNode.getLeftCenterCoordinates());
  }

  private getMatriarchalConnection(rootNode: FamilyTreeNode, parent: FamilyTreeNode): Connection {
    return new Connection(rootNode.getRightCenterCoordinates(), parent.getLeftCenterCoordinates());
  }
}

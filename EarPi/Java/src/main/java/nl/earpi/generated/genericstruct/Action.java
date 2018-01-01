/**
 * Autogenerated by Thrift Compiler (0.10.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package nl.earpi.generated.genericstruct;

@SuppressWarnings({"cast", "rawtypes", "serial", "unchecked", "unused"})
@javax.annotation.Generated(value = "Autogenerated by Thrift Compiler (0.10.0)", date = "2017-12-31")
public class Action implements org.apache.thrift.TBase<Action, Action._Fields>, java.io.Serializable, Cloneable, Comparable<Action> {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("Action");

  private static final org.apache.thrift.protocol.TField ACTION_ENUM_FIELD_DESC = new org.apache.thrift.protocol.TField("actionEnum", org.apache.thrift.protocol.TType.I32, (short)1);
  private static final org.apache.thrift.protocol.TField UI_TYPE_FIELD_DESC = new org.apache.thrift.protocol.TField("uiType", org.apache.thrift.protocol.TType.I32, (short)2);
  private static final org.apache.thrift.protocol.TField NAME_FIELD_DESC = new org.apache.thrift.protocol.TField("name", org.apache.thrift.protocol.TType.STRING, (short)3);

  private static final org.apache.thrift.scheme.SchemeFactory STANDARD_SCHEME_FACTORY = new ActionStandardSchemeFactory();
  private static final org.apache.thrift.scheme.SchemeFactory TUPLE_SCHEME_FACTORY = new ActionTupleSchemeFactory();

  /**
   * 
   * @see ActionEnum
   */
  public ActionEnum actionEnum; // required
  /**
   * 
   * @see UiType
   */
  public UiType uiType; // required
  public java.lang.String name; // required

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    /**
     * 
     * @see ActionEnum
     */
    ACTION_ENUM((short)1, "actionEnum"),
    /**
     * 
     * @see UiType
     */
    UI_TYPE((short)2, "uiType"),
    NAME((short)3, "name");

    private static final java.util.Map<java.lang.String, _Fields> byName = new java.util.HashMap<java.lang.String, _Fields>();

    static {
      for (_Fields field : java.util.EnumSet.allOf(_Fields.class)) {
        byName.put(field.getFieldName(), field);
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, or null if its not found.
     */
    public static _Fields findByThriftId(int fieldId) {
      switch(fieldId) {
        case 1: // ACTION_ENUM
          return ACTION_ENUM;
        case 2: // UI_TYPE
          return UI_TYPE;
        case 3: // NAME
          return NAME;
        default:
          return null;
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, throwing an exception
     * if it is not found.
     */
    public static _Fields findByThriftIdOrThrow(int fieldId) {
      _Fields fields = findByThriftId(fieldId);
      if (fields == null) throw new java.lang.IllegalArgumentException("Field " + fieldId + " doesn't exist!");
      return fields;
    }

    /**
     * Find the _Fields constant that matches name, or null if its not found.
     */
    public static _Fields findByName(java.lang.String name) {
      return byName.get(name);
    }

    private final short _thriftId;
    private final java.lang.String _fieldName;

    _Fields(short thriftId, java.lang.String fieldName) {
      _thriftId = thriftId;
      _fieldName = fieldName;
    }

    public short getThriftFieldId() {
      return _thriftId;
    }

    public java.lang.String getFieldName() {
      return _fieldName;
    }
  }

  // isset id assignments
  public static final java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new java.util.EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.ACTION_ENUM, new org.apache.thrift.meta_data.FieldMetaData("actionEnum", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.EnumMetaData(org.apache.thrift.protocol.TType.ENUM, ActionEnum.class)));
    tmpMap.put(_Fields.UI_TYPE, new org.apache.thrift.meta_data.FieldMetaData("uiType", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.EnumMetaData(org.apache.thrift.protocol.TType.ENUM, UiType.class)));
    tmpMap.put(_Fields.NAME, new org.apache.thrift.meta_data.FieldMetaData("name", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    metaDataMap = java.util.Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(Action.class, metaDataMap);
  }

  public Action() {
  }

  public Action(
    ActionEnum actionEnum,
    UiType uiType,
    java.lang.String name)
  {
    this();
    this.actionEnum = actionEnum;
    this.uiType = uiType;
    this.name = name;
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public Action(Action other) {
    if (other.isSetActionEnum()) {
      this.actionEnum = other.actionEnum;
    }
    if (other.isSetUiType()) {
      this.uiType = other.uiType;
    }
    if (other.isSetName()) {
      this.name = other.name;
    }
  }

  public Action deepCopy() {
    return new Action(this);
  }

  @Override
  public void clear() {
    this.actionEnum = null;
    this.uiType = null;
    this.name = null;
  }

  /**
   * 
   * @see ActionEnum
   */
  public ActionEnum getActionEnum() {
    return this.actionEnum;
  }

  /**
   * 
   * @see ActionEnum
   */
  public Action setActionEnum(ActionEnum actionEnum) {
    this.actionEnum = actionEnum;
    return this;
  }

  public void unsetActionEnum() {
    this.actionEnum = null;
  }

  /** Returns true if field actionEnum is set (has been assigned a value) and false otherwise */
  public boolean isSetActionEnum() {
    return this.actionEnum != null;
  }

  public void setActionEnumIsSet(boolean value) {
    if (!value) {
      this.actionEnum = null;
    }
  }

  /**
   * 
   * @see UiType
   */
  public UiType getUiType() {
    return this.uiType;
  }

  /**
   * 
   * @see UiType
   */
  public Action setUiType(UiType uiType) {
    this.uiType = uiType;
    return this;
  }

  public void unsetUiType() {
    this.uiType = null;
  }

  /** Returns true if field uiType is set (has been assigned a value) and false otherwise */
  public boolean isSetUiType() {
    return this.uiType != null;
  }

  public void setUiTypeIsSet(boolean value) {
    if (!value) {
      this.uiType = null;
    }
  }

  public java.lang.String getName() {
    return this.name;
  }

  public Action setName(java.lang.String name) {
    this.name = name;
    return this;
  }

  public void unsetName() {
    this.name = null;
  }

  /** Returns true if field name is set (has been assigned a value) and false otherwise */
  public boolean isSetName() {
    return this.name != null;
  }

  public void setNameIsSet(boolean value) {
    if (!value) {
      this.name = null;
    }
  }

  public void setFieldValue(_Fields field, java.lang.Object value) {
    switch (field) {
    case ACTION_ENUM:
      if (value == null) {
        unsetActionEnum();
      } else {
        setActionEnum((ActionEnum)value);
      }
      break;

    case UI_TYPE:
      if (value == null) {
        unsetUiType();
      } else {
        setUiType((UiType)value);
      }
      break;

    case NAME:
      if (value == null) {
        unsetName();
      } else {
        setName((java.lang.String)value);
      }
      break;

    }
  }

  public java.lang.Object getFieldValue(_Fields field) {
    switch (field) {
    case ACTION_ENUM:
      return getActionEnum();

    case UI_TYPE:
      return getUiType();

    case NAME:
      return getName();

    }
    throw new java.lang.IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new java.lang.IllegalArgumentException();
    }

    switch (field) {
    case ACTION_ENUM:
      return isSetActionEnum();
    case UI_TYPE:
      return isSetUiType();
    case NAME:
      return isSetName();
    }
    throw new java.lang.IllegalStateException();
  }

  @Override
  public boolean equals(java.lang.Object that) {
    if (that == null)
      return false;
    if (that instanceof Action)
      return this.equals((Action)that);
    return false;
  }

  public boolean equals(Action that) {
    if (that == null)
      return false;
    if (this == that)
      return true;

    boolean this_present_actionEnum = true && this.isSetActionEnum();
    boolean that_present_actionEnum = true && that.isSetActionEnum();
    if (this_present_actionEnum || that_present_actionEnum) {
      if (!(this_present_actionEnum && that_present_actionEnum))
        return false;
      if (!this.actionEnum.equals(that.actionEnum))
        return false;
    }

    boolean this_present_uiType = true && this.isSetUiType();
    boolean that_present_uiType = true && that.isSetUiType();
    if (this_present_uiType || that_present_uiType) {
      if (!(this_present_uiType && that_present_uiType))
        return false;
      if (!this.uiType.equals(that.uiType))
        return false;
    }

    boolean this_present_name = true && this.isSetName();
    boolean that_present_name = true && that.isSetName();
    if (this_present_name || that_present_name) {
      if (!(this_present_name && that_present_name))
        return false;
      if (!this.name.equals(that.name))
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    int hashCode = 1;

    hashCode = hashCode * 8191 + ((isSetActionEnum()) ? 131071 : 524287);
    if (isSetActionEnum())
      hashCode = hashCode * 8191 + actionEnum.getValue();

    hashCode = hashCode * 8191 + ((isSetUiType()) ? 131071 : 524287);
    if (isSetUiType())
      hashCode = hashCode * 8191 + uiType.getValue();

    hashCode = hashCode * 8191 + ((isSetName()) ? 131071 : 524287);
    if (isSetName())
      hashCode = hashCode * 8191 + name.hashCode();

    return hashCode;
  }

  @Override
  public int compareTo(Action other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;

    lastComparison = java.lang.Boolean.valueOf(isSetActionEnum()).compareTo(other.isSetActionEnum());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetActionEnum()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.actionEnum, other.actionEnum);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetUiType()).compareTo(other.isSetUiType());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetUiType()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.uiType, other.uiType);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetName()).compareTo(other.isSetName());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetName()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.name, other.name);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    return 0;
  }

  public _Fields fieldForId(int fieldId) {
    return _Fields.findByThriftId(fieldId);
  }

  public void read(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    scheme(iprot).read(iprot, this);
  }

  public void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
    scheme(oprot).write(oprot, this);
  }

  @Override
  public java.lang.String toString() {
    java.lang.StringBuilder sb = new java.lang.StringBuilder("Action(");
    boolean first = true;

    sb.append("actionEnum:");
    if (this.actionEnum == null) {
      sb.append("null");
    } else {
      sb.append(this.actionEnum);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("uiType:");
    if (this.uiType == null) {
      sb.append("null");
    } else {
      sb.append(this.uiType);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("name:");
    if (this.name == null) {
      sb.append("null");
    } else {
      sb.append(this.name);
    }
    first = false;
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
    // check for sub-struct validity
  }

  private void writeObject(java.io.ObjectOutputStream out) throws java.io.IOException {
    try {
      write(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(out)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private void readObject(java.io.ObjectInputStream in) throws java.io.IOException, java.lang.ClassNotFoundException {
    try {
      read(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(in)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private static class ActionStandardSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public ActionStandardScheme getScheme() {
      return new ActionStandardScheme();
    }
  }

  private static class ActionStandardScheme extends org.apache.thrift.scheme.StandardScheme<Action> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, Action struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // ACTION_ENUM
            if (schemeField.type == org.apache.thrift.protocol.TType.I32) {
              struct.actionEnum = nl.earpi.generated.genericstruct.ActionEnum.findByValue(iprot.readI32());
              struct.setActionEnumIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // UI_TYPE
            if (schemeField.type == org.apache.thrift.protocol.TType.I32) {
              struct.uiType = nl.earpi.generated.genericstruct.UiType.findByValue(iprot.readI32());
              struct.setUiTypeIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 3: // NAME
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.name = iprot.readString();
              struct.setNameIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          default:
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
        }
        iprot.readFieldEnd();
      }
      iprot.readStructEnd();

      // check for required fields of primitive type, which can't be checked in the validate method
      struct.validate();
    }

    public void write(org.apache.thrift.protocol.TProtocol oprot, Action struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      if (struct.actionEnum != null) {
        oprot.writeFieldBegin(ACTION_ENUM_FIELD_DESC);
        oprot.writeI32(struct.actionEnum.getValue());
        oprot.writeFieldEnd();
      }
      if (struct.uiType != null) {
        oprot.writeFieldBegin(UI_TYPE_FIELD_DESC);
        oprot.writeI32(struct.uiType.getValue());
        oprot.writeFieldEnd();
      }
      if (struct.name != null) {
        oprot.writeFieldBegin(NAME_FIELD_DESC);
        oprot.writeString(struct.name);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class ActionTupleSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public ActionTupleScheme getScheme() {
      return new ActionTupleScheme();
    }
  }

  private static class ActionTupleScheme extends org.apache.thrift.scheme.TupleScheme<Action> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, Action struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol oprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      java.util.BitSet optionals = new java.util.BitSet();
      if (struct.isSetActionEnum()) {
        optionals.set(0);
      }
      if (struct.isSetUiType()) {
        optionals.set(1);
      }
      if (struct.isSetName()) {
        optionals.set(2);
      }
      oprot.writeBitSet(optionals, 3);
      if (struct.isSetActionEnum()) {
        oprot.writeI32(struct.actionEnum.getValue());
      }
      if (struct.isSetUiType()) {
        oprot.writeI32(struct.uiType.getValue());
      }
      if (struct.isSetName()) {
        oprot.writeString(struct.name);
      }
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, Action struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol iprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      java.util.BitSet incoming = iprot.readBitSet(3);
      if (incoming.get(0)) {
        struct.actionEnum = nl.earpi.generated.genericstruct.ActionEnum.findByValue(iprot.readI32());
        struct.setActionEnumIsSet(true);
      }
      if (incoming.get(1)) {
        struct.uiType = nl.earpi.generated.genericstruct.UiType.findByValue(iprot.readI32());
        struct.setUiTypeIsSet(true);
      }
      if (incoming.get(2)) {
        struct.name = iprot.readString();
        struct.setNameIsSet(true);
      }
    }
  }

  private static <S extends org.apache.thrift.scheme.IScheme> S scheme(org.apache.thrift.protocol.TProtocol proto) {
    return (org.apache.thrift.scheme.StandardScheme.class.equals(proto.getScheme()) ? STANDARD_SCHEME_FACTORY : TUPLE_SCHEME_FACTORY).getScheme();
  }
}


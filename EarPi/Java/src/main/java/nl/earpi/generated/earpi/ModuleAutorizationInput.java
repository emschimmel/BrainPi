/**
 * Autogenerated by Thrift Compiler (0.10.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package nl.earpi.generated.earpi;

@SuppressWarnings({"cast", "rawtypes", "serial", "unchecked", "unused"})
@javax.annotation.Generated(value = "Autogenerated by Thrift Compiler (0.10.0)", date = "2017-12-31")
public class ModuleAutorizationInput implements org.apache.thrift.TBase<ModuleAutorizationInput, ModuleAutorizationInput._Fields>, java.io.Serializable, Cloneable, Comparable<ModuleAutorizationInput> {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("ModuleAutorizationInput");

  private static final org.apache.thrift.protocol.TField MODULE_MAP_FIELD_DESC = new org.apache.thrift.protocol.TField("moduleMap", org.apache.thrift.protocol.TType.MAP, (short)1);
  private static final org.apache.thrift.protocol.TField PERSON_FIELD_DESC = new org.apache.thrift.protocol.TField("person", org.apache.thrift.protocol.TType.STRING, (short)2);
  private static final org.apache.thrift.protocol.TField DEVICE_TOKEN_FIELD_DESC = new org.apache.thrift.protocol.TField("deviceToken", org.apache.thrift.protocol.TType.STRING, (short)3);
  private static final org.apache.thrift.protocol.TField TOKEN_FIELD_DESC = new org.apache.thrift.protocol.TField("token", org.apache.thrift.protocol.TType.STRING, (short)4);

  private static final org.apache.thrift.scheme.SchemeFactory STANDARD_SCHEME_FACTORY = new ModuleAutorizationInputStandardSchemeFactory();
  private static final org.apache.thrift.scheme.SchemeFactory TUPLE_SCHEME_FACTORY = new ModuleAutorizationInputTupleSchemeFactory();

  public java.util.Map<nl.earpi.generated.genericstruct.ActionEnum,java.lang.Boolean> moduleMap; // required
  public java.lang.String person; // required
  public java.lang.String deviceToken; // required
  public java.lang.String token; // optional

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    MODULE_MAP((short)1, "moduleMap"),
    PERSON((short)2, "person"),
    DEVICE_TOKEN((short)3, "deviceToken"),
    TOKEN((short)4, "token");

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
        case 1: // MODULE_MAP
          return MODULE_MAP;
        case 2: // PERSON
          return PERSON;
        case 3: // DEVICE_TOKEN
          return DEVICE_TOKEN;
        case 4: // TOKEN
          return TOKEN;
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
  private static final _Fields optionals[] = {_Fields.TOKEN};
  public static final java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new java.util.EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.MODULE_MAP, new org.apache.thrift.meta_data.FieldMetaData("moduleMap", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.MapMetaData(org.apache.thrift.protocol.TType.MAP, 
            new org.apache.thrift.meta_data.EnumMetaData(org.apache.thrift.protocol.TType.ENUM, nl.earpi.generated.genericstruct.ActionEnum.class), 
            new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.BOOL))));
    tmpMap.put(_Fields.PERSON, new org.apache.thrift.meta_data.FieldMetaData("person", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.DEVICE_TOKEN, new org.apache.thrift.meta_data.FieldMetaData("deviceToken", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.TOKEN, new org.apache.thrift.meta_data.FieldMetaData("token", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    metaDataMap = java.util.Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(ModuleAutorizationInput.class, metaDataMap);
  }

  public ModuleAutorizationInput() {
  }

  public ModuleAutorizationInput(
    java.util.Map<nl.earpi.generated.genericstruct.ActionEnum,java.lang.Boolean> moduleMap,
    java.lang.String person,
    java.lang.String deviceToken)
  {
    this();
    this.moduleMap = moduleMap;
    this.person = person;
    this.deviceToken = deviceToken;
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public ModuleAutorizationInput(ModuleAutorizationInput other) {
    if (other.isSetModuleMap()) {
      java.util.Map<nl.earpi.generated.genericstruct.ActionEnum,java.lang.Boolean> __this__moduleMap = new java.util.HashMap<nl.earpi.generated.genericstruct.ActionEnum,java.lang.Boolean>(other.moduleMap.size());
      for (java.util.Map.Entry<nl.earpi.generated.genericstruct.ActionEnum, java.lang.Boolean> other_element : other.moduleMap.entrySet()) {

        nl.earpi.generated.genericstruct.ActionEnum other_element_key = other_element.getKey();
        java.lang.Boolean other_element_value = other_element.getValue();

        nl.earpi.generated.genericstruct.ActionEnum __this__moduleMap_copy_key = other_element_key;

        java.lang.Boolean __this__moduleMap_copy_value = other_element_value;

        __this__moduleMap.put(__this__moduleMap_copy_key, __this__moduleMap_copy_value);
      }
      this.moduleMap = __this__moduleMap;
    }
    if (other.isSetPerson()) {
      this.person = other.person;
    }
    if (other.isSetDeviceToken()) {
      this.deviceToken = other.deviceToken;
    }
    if (other.isSetToken()) {
      this.token = other.token;
    }
  }

  public ModuleAutorizationInput deepCopy() {
    return new ModuleAutorizationInput(this);
  }

  @Override
  public void clear() {
    this.moduleMap = null;
    this.person = null;
    this.deviceToken = null;
    this.token = null;
  }

  public int getModuleMapSize() {
    return (this.moduleMap == null) ? 0 : this.moduleMap.size();
  }

  public void putToModuleMap(nl.earpi.generated.genericstruct.ActionEnum key, boolean val) {
    if (this.moduleMap == null) {
      this.moduleMap = new java.util.HashMap<nl.earpi.generated.genericstruct.ActionEnum,java.lang.Boolean>();
    }
    this.moduleMap.put(key, val);
  }

  public java.util.Map<nl.earpi.generated.genericstruct.ActionEnum,java.lang.Boolean> getModuleMap() {
    return this.moduleMap;
  }

  public ModuleAutorizationInput setModuleMap(java.util.Map<nl.earpi.generated.genericstruct.ActionEnum,java.lang.Boolean> moduleMap) {
    this.moduleMap = moduleMap;
    return this;
  }

  public void unsetModuleMap() {
    this.moduleMap = null;
  }

  /** Returns true if field moduleMap is set (has been assigned a value) and false otherwise */
  public boolean isSetModuleMap() {
    return this.moduleMap != null;
  }

  public void setModuleMapIsSet(boolean value) {
    if (!value) {
      this.moduleMap = null;
    }
  }

  public java.lang.String getPerson() {
    return this.person;
  }

  public ModuleAutorizationInput setPerson(java.lang.String person) {
    this.person = person;
    return this;
  }

  public void unsetPerson() {
    this.person = null;
  }

  /** Returns true if field person is set (has been assigned a value) and false otherwise */
  public boolean isSetPerson() {
    return this.person != null;
  }

  public void setPersonIsSet(boolean value) {
    if (!value) {
      this.person = null;
    }
  }

  public java.lang.String getDeviceToken() {
    return this.deviceToken;
  }

  public ModuleAutorizationInput setDeviceToken(java.lang.String deviceToken) {
    this.deviceToken = deviceToken;
    return this;
  }

  public void unsetDeviceToken() {
    this.deviceToken = null;
  }

  /** Returns true if field deviceToken is set (has been assigned a value) and false otherwise */
  public boolean isSetDeviceToken() {
    return this.deviceToken != null;
  }

  public void setDeviceTokenIsSet(boolean value) {
    if (!value) {
      this.deviceToken = null;
    }
  }

  public java.lang.String getToken() {
    return this.token;
  }

  public ModuleAutorizationInput setToken(java.lang.String token) {
    this.token = token;
    return this;
  }

  public void unsetToken() {
    this.token = null;
  }

  /** Returns true if field token is set (has been assigned a value) and false otherwise */
  public boolean isSetToken() {
    return this.token != null;
  }

  public void setTokenIsSet(boolean value) {
    if (!value) {
      this.token = null;
    }
  }

  public void setFieldValue(_Fields field, java.lang.Object value) {
    switch (field) {
    case MODULE_MAP:
      if (value == null) {
        unsetModuleMap();
      } else {
        setModuleMap((java.util.Map<nl.earpi.generated.genericstruct.ActionEnum,java.lang.Boolean>)value);
      }
      break;

    case PERSON:
      if (value == null) {
        unsetPerson();
      } else {
        setPerson((java.lang.String)value);
      }
      break;

    case DEVICE_TOKEN:
      if (value == null) {
        unsetDeviceToken();
      } else {
        setDeviceToken((java.lang.String)value);
      }
      break;

    case TOKEN:
      if (value == null) {
        unsetToken();
      } else {
        setToken((java.lang.String)value);
      }
      break;

    }
  }

  public java.lang.Object getFieldValue(_Fields field) {
    switch (field) {
    case MODULE_MAP:
      return getModuleMap();

    case PERSON:
      return getPerson();

    case DEVICE_TOKEN:
      return getDeviceToken();

    case TOKEN:
      return getToken();

    }
    throw new java.lang.IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new java.lang.IllegalArgumentException();
    }

    switch (field) {
    case MODULE_MAP:
      return isSetModuleMap();
    case PERSON:
      return isSetPerson();
    case DEVICE_TOKEN:
      return isSetDeviceToken();
    case TOKEN:
      return isSetToken();
    }
    throw new java.lang.IllegalStateException();
  }

  @Override
  public boolean equals(java.lang.Object that) {
    if (that == null)
      return false;
    if (that instanceof ModuleAutorizationInput)
      return this.equals((ModuleAutorizationInput)that);
    return false;
  }

  public boolean equals(ModuleAutorizationInput that) {
    if (that == null)
      return false;
    if (this == that)
      return true;

    boolean this_present_moduleMap = true && this.isSetModuleMap();
    boolean that_present_moduleMap = true && that.isSetModuleMap();
    if (this_present_moduleMap || that_present_moduleMap) {
      if (!(this_present_moduleMap && that_present_moduleMap))
        return false;
      if (!this.moduleMap.equals(that.moduleMap))
        return false;
    }

    boolean this_present_person = true && this.isSetPerson();
    boolean that_present_person = true && that.isSetPerson();
    if (this_present_person || that_present_person) {
      if (!(this_present_person && that_present_person))
        return false;
      if (!this.person.equals(that.person))
        return false;
    }

    boolean this_present_deviceToken = true && this.isSetDeviceToken();
    boolean that_present_deviceToken = true && that.isSetDeviceToken();
    if (this_present_deviceToken || that_present_deviceToken) {
      if (!(this_present_deviceToken && that_present_deviceToken))
        return false;
      if (!this.deviceToken.equals(that.deviceToken))
        return false;
    }

    boolean this_present_token = true && this.isSetToken();
    boolean that_present_token = true && that.isSetToken();
    if (this_present_token || that_present_token) {
      if (!(this_present_token && that_present_token))
        return false;
      if (!this.token.equals(that.token))
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    int hashCode = 1;

    hashCode = hashCode * 8191 + ((isSetModuleMap()) ? 131071 : 524287);
    if (isSetModuleMap())
      hashCode = hashCode * 8191 + moduleMap.hashCode();

    hashCode = hashCode * 8191 + ((isSetPerson()) ? 131071 : 524287);
    if (isSetPerson())
      hashCode = hashCode * 8191 + person.hashCode();

    hashCode = hashCode * 8191 + ((isSetDeviceToken()) ? 131071 : 524287);
    if (isSetDeviceToken())
      hashCode = hashCode * 8191 + deviceToken.hashCode();

    hashCode = hashCode * 8191 + ((isSetToken()) ? 131071 : 524287);
    if (isSetToken())
      hashCode = hashCode * 8191 + token.hashCode();

    return hashCode;
  }

  @Override
  public int compareTo(ModuleAutorizationInput other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;

    lastComparison = java.lang.Boolean.valueOf(isSetModuleMap()).compareTo(other.isSetModuleMap());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetModuleMap()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.moduleMap, other.moduleMap);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetPerson()).compareTo(other.isSetPerson());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetPerson()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.person, other.person);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetDeviceToken()).compareTo(other.isSetDeviceToken());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetDeviceToken()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.deviceToken, other.deviceToken);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetToken()).compareTo(other.isSetToken());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetToken()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.token, other.token);
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
    java.lang.StringBuilder sb = new java.lang.StringBuilder("ModuleAutorizationInput(");
    boolean first = true;

    sb.append("moduleMap:");
    if (this.moduleMap == null) {
      sb.append("null");
    } else {
      sb.append(this.moduleMap);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("person:");
    if (this.person == null) {
      sb.append("null");
    } else {
      sb.append(this.person);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("deviceToken:");
    if (this.deviceToken == null) {
      sb.append("null");
    } else {
      sb.append(this.deviceToken);
    }
    first = false;
    if (isSetToken()) {
      if (!first) sb.append(", ");
      sb.append("token:");
      if (this.token == null) {
        sb.append("null");
      } else {
        sb.append(this.token);
      }
      first = false;
    }
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
    if (moduleMap == null) {
      throw new org.apache.thrift.protocol.TProtocolException("Required field 'moduleMap' was not present! Struct: " + toString());
    }
    if (person == null) {
      throw new org.apache.thrift.protocol.TProtocolException("Required field 'person' was not present! Struct: " + toString());
    }
    if (deviceToken == null) {
      throw new org.apache.thrift.protocol.TProtocolException("Required field 'deviceToken' was not present! Struct: " + toString());
    }
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

  private static class ModuleAutorizationInputStandardSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public ModuleAutorizationInputStandardScheme getScheme() {
      return new ModuleAutorizationInputStandardScheme();
    }
  }

  private static class ModuleAutorizationInputStandardScheme extends org.apache.thrift.scheme.StandardScheme<ModuleAutorizationInput> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, ModuleAutorizationInput struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // MODULE_MAP
            if (schemeField.type == org.apache.thrift.protocol.TType.MAP) {
              {
                org.apache.thrift.protocol.TMap _map10 = iprot.readMapBegin();
                struct.moduleMap = new java.util.HashMap<nl.earpi.generated.genericstruct.ActionEnum,java.lang.Boolean>(2*_map10.size);
                nl.earpi.generated.genericstruct.ActionEnum _key11;
                boolean _val12;
                for (int _i13 = 0; _i13 < _map10.size; ++_i13)
                {
                  _key11 = nl.earpi.generated.genericstruct.ActionEnum.findByValue(iprot.readI32());
                  _val12 = iprot.readBool();
                  struct.moduleMap.put(_key11, _val12);
                }
                iprot.readMapEnd();
              }
              struct.setModuleMapIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // PERSON
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.person = iprot.readString();
              struct.setPersonIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 3: // DEVICE_TOKEN
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.deviceToken = iprot.readString();
              struct.setDeviceTokenIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 4: // TOKEN
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.token = iprot.readString();
              struct.setTokenIsSet(true);
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

    public void write(org.apache.thrift.protocol.TProtocol oprot, ModuleAutorizationInput struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      if (struct.moduleMap != null) {
        oprot.writeFieldBegin(MODULE_MAP_FIELD_DESC);
        {
          oprot.writeMapBegin(new org.apache.thrift.protocol.TMap(org.apache.thrift.protocol.TType.I32, org.apache.thrift.protocol.TType.BOOL, struct.moduleMap.size()));
          for (java.util.Map.Entry<nl.earpi.generated.genericstruct.ActionEnum, java.lang.Boolean> _iter14 : struct.moduleMap.entrySet())
          {
            oprot.writeI32(_iter14.getKey().getValue());
            oprot.writeBool(_iter14.getValue());
          }
          oprot.writeMapEnd();
        }
        oprot.writeFieldEnd();
      }
      if (struct.person != null) {
        oprot.writeFieldBegin(PERSON_FIELD_DESC);
        oprot.writeString(struct.person);
        oprot.writeFieldEnd();
      }
      if (struct.deviceToken != null) {
        oprot.writeFieldBegin(DEVICE_TOKEN_FIELD_DESC);
        oprot.writeString(struct.deviceToken);
        oprot.writeFieldEnd();
      }
      if (struct.token != null) {
        if (struct.isSetToken()) {
          oprot.writeFieldBegin(TOKEN_FIELD_DESC);
          oprot.writeString(struct.token);
          oprot.writeFieldEnd();
        }
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class ModuleAutorizationInputTupleSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public ModuleAutorizationInputTupleScheme getScheme() {
      return new ModuleAutorizationInputTupleScheme();
    }
  }

  private static class ModuleAutorizationInputTupleScheme extends org.apache.thrift.scheme.TupleScheme<ModuleAutorizationInput> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, ModuleAutorizationInput struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol oprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      {
        oprot.writeI32(struct.moduleMap.size());
        for (java.util.Map.Entry<nl.earpi.generated.genericstruct.ActionEnum, java.lang.Boolean> _iter15 : struct.moduleMap.entrySet())
        {
          oprot.writeI32(_iter15.getKey().getValue());
          oprot.writeBool(_iter15.getValue());
        }
      }
      oprot.writeString(struct.person);
      oprot.writeString(struct.deviceToken);
      java.util.BitSet optionals = new java.util.BitSet();
      if (struct.isSetToken()) {
        optionals.set(0);
      }
      oprot.writeBitSet(optionals, 1);
      if (struct.isSetToken()) {
        oprot.writeString(struct.token);
      }
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, ModuleAutorizationInput struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol iprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      {
        org.apache.thrift.protocol.TMap _map16 = new org.apache.thrift.protocol.TMap(org.apache.thrift.protocol.TType.I32, org.apache.thrift.protocol.TType.BOOL, iprot.readI32());
        struct.moduleMap = new java.util.HashMap<nl.earpi.generated.genericstruct.ActionEnum,java.lang.Boolean>(2*_map16.size);
        nl.earpi.generated.genericstruct.ActionEnum _key17;
        boolean _val18;
        for (int _i19 = 0; _i19 < _map16.size; ++_i19)
        {
          _key17 = nl.earpi.generated.genericstruct.ActionEnum.findByValue(iprot.readI32());
          _val18 = iprot.readBool();
          struct.moduleMap.put(_key17, _val18);
        }
      }
      struct.setModuleMapIsSet(true);
      struct.person = iprot.readString();
      struct.setPersonIsSet(true);
      struct.deviceToken = iprot.readString();
      struct.setDeviceTokenIsSet(true);
      java.util.BitSet incoming = iprot.readBitSet(1);
      if (incoming.get(0)) {
        struct.token = iprot.readString();
        struct.setTokenIsSet(true);
      }
    }
  }

  private static <S extends org.apache.thrift.scheme.IScheme> S scheme(org.apache.thrift.protocol.TProtocol proto) {
    return (org.apache.thrift.scheme.StandardScheme.class.equals(proto.getScheme()) ? STANDARD_SCHEME_FACTORY : TUPLE_SCHEME_FACTORY).getScheme();
  }
}


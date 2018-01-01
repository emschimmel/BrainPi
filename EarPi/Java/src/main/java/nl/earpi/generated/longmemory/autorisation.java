/**
 * Autogenerated by Thrift Compiler (0.10.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package nl.earpi.generated.longmemory;

@SuppressWarnings({"cast", "rawtypes", "serial", "unchecked", "unused"})
@javax.annotation.Generated(value = "Autogenerated by Thrift Compiler (0.10.0)", date = "2017-12-29")
public class autorisation implements org.apache.thrift.TBase<autorisation, autorisation._Fields>, java.io.Serializable, Cloneable, Comparable<autorisation> {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("autorisation");

  private static final org.apache.thrift.protocol.TField WRITE_FIELD_DESC = new org.apache.thrift.protocol.TField("write", org.apache.thrift.protocol.TType.BOOL, (short)1);
  private static final org.apache.thrift.protocol.TField ENABLED_FIELD_DESC = new org.apache.thrift.protocol.TField("enabled", org.apache.thrift.protocol.TType.BOOL, (short)2);
  private static final org.apache.thrift.protocol.TField MODULE_CONFIG_FIELD_DESC = new org.apache.thrift.protocol.TField("module_config", org.apache.thrift.protocol.TType.STRING, (short)3);

  private static final org.apache.thrift.scheme.SchemeFactory STANDARD_SCHEME_FACTORY = new autorisationStandardSchemeFactory();
  private static final org.apache.thrift.scheme.SchemeFactory TUPLE_SCHEME_FACTORY = new autorisationTupleSchemeFactory();

  public boolean write; // required
  public boolean enabled; // required
  public java.nio.ByteBuffer module_config; // optional

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    WRITE((short)1, "write"),
    ENABLED((short)2, "enabled"),
    MODULE_CONFIG((short)3, "module_config");

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
        case 1: // WRITE
          return WRITE;
        case 2: // ENABLED
          return ENABLED;
        case 3: // MODULE_CONFIG
          return MODULE_CONFIG;
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
  private static final int __WRITE_ISSET_ID = 0;
  private static final int __ENABLED_ISSET_ID = 1;
  private byte __isset_bitfield = 0;
  private static final _Fields optionals[] = {_Fields.MODULE_CONFIG};
  public static final java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new java.util.EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.WRITE, new org.apache.thrift.meta_data.FieldMetaData("write", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.BOOL)));
    tmpMap.put(_Fields.ENABLED, new org.apache.thrift.meta_data.FieldMetaData("enabled", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.BOOL)));
    tmpMap.put(_Fields.MODULE_CONFIG, new org.apache.thrift.meta_data.FieldMetaData("module_config", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING        , true)));
    metaDataMap = java.util.Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(autorisation.class, metaDataMap);
  }

  public autorisation() {
  }

  public autorisation(
    boolean write,
    boolean enabled)
  {
    this();
    this.write = write;
    setWriteIsSet(true);
    this.enabled = enabled;
    setEnabledIsSet(true);
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public autorisation(autorisation other) {
    __isset_bitfield = other.__isset_bitfield;
    this.write = other.write;
    this.enabled = other.enabled;
    if (other.isSetModule_config()) {
      this.module_config = org.apache.thrift.TBaseHelper.copyBinary(other.module_config);
    }
  }

  public autorisation deepCopy() {
    return new autorisation(this);
  }

  @Override
  public void clear() {
    setWriteIsSet(false);
    this.write = false;
    setEnabledIsSet(false);
    this.enabled = false;
    this.module_config = null;
  }

  public boolean isWrite() {
    return this.write;
  }

  public autorisation setWrite(boolean write) {
    this.write = write;
    setWriteIsSet(true);
    return this;
  }

  public void unsetWrite() {
    __isset_bitfield = org.apache.thrift.EncodingUtils.clearBit(__isset_bitfield, __WRITE_ISSET_ID);
  }

  /** Returns true if field write is set (has been assigned a value) and false otherwise */
  public boolean isSetWrite() {
    return org.apache.thrift.EncodingUtils.testBit(__isset_bitfield, __WRITE_ISSET_ID);
  }

  public void setWriteIsSet(boolean value) {
    __isset_bitfield = org.apache.thrift.EncodingUtils.setBit(__isset_bitfield, __WRITE_ISSET_ID, value);
  }

  public boolean isEnabled() {
    return this.enabled;
  }

  public autorisation setEnabled(boolean enabled) {
    this.enabled = enabled;
    setEnabledIsSet(true);
    return this;
  }

  public void unsetEnabled() {
    __isset_bitfield = org.apache.thrift.EncodingUtils.clearBit(__isset_bitfield, __ENABLED_ISSET_ID);
  }

  /** Returns true if field enabled is set (has been assigned a value) and false otherwise */
  public boolean isSetEnabled() {
    return org.apache.thrift.EncodingUtils.testBit(__isset_bitfield, __ENABLED_ISSET_ID);
  }

  public void setEnabledIsSet(boolean value) {
    __isset_bitfield = org.apache.thrift.EncodingUtils.setBit(__isset_bitfield, __ENABLED_ISSET_ID, value);
  }

  public byte[] getModule_config() {
    setModule_config(org.apache.thrift.TBaseHelper.rightSize(module_config));
    return module_config == null ? null : module_config.array();
  }

  public java.nio.ByteBuffer bufferForModule_config() {
    return org.apache.thrift.TBaseHelper.copyBinary(module_config);
  }

  public autorisation setModule_config(byte[] module_config) {
    this.module_config = module_config == null ? (java.nio.ByteBuffer)null : java.nio.ByteBuffer.wrap(module_config.clone());
    return this;
  }

  public autorisation setModule_config(java.nio.ByteBuffer module_config) {
    this.module_config = org.apache.thrift.TBaseHelper.copyBinary(module_config);
    return this;
  }

  public void unsetModule_config() {
    this.module_config = null;
  }

  /** Returns true if field module_config is set (has been assigned a value) and false otherwise */
  public boolean isSetModule_config() {
    return this.module_config != null;
  }

  public void setModule_configIsSet(boolean value) {
    if (!value) {
      this.module_config = null;
    }
  }

  public void setFieldValue(_Fields field, java.lang.Object value) {
    switch (field) {
    case WRITE:
      if (value == null) {
        unsetWrite();
      } else {
        setWrite((java.lang.Boolean)value);
      }
      break;

    case ENABLED:
      if (value == null) {
        unsetEnabled();
      } else {
        setEnabled((java.lang.Boolean)value);
      }
      break;

    case MODULE_CONFIG:
      if (value == null) {
        unsetModule_config();
      } else {
        if (value instanceof byte[]) {
          setModule_config((byte[])value);
        } else {
          setModule_config((java.nio.ByteBuffer)value);
        }
      }
      break;

    }
  }

  public java.lang.Object getFieldValue(_Fields field) {
    switch (field) {
    case WRITE:
      return isWrite();

    case ENABLED:
      return isEnabled();

    case MODULE_CONFIG:
      return getModule_config();

    }
    throw new java.lang.IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new java.lang.IllegalArgumentException();
    }

    switch (field) {
    case WRITE:
      return isSetWrite();
    case ENABLED:
      return isSetEnabled();
    case MODULE_CONFIG:
      return isSetModule_config();
    }
    throw new java.lang.IllegalStateException();
  }

  @Override
  public boolean equals(java.lang.Object that) {
    if (that == null)
      return false;
    if (that instanceof autorisation)
      return this.equals((autorisation)that);
    return false;
  }

  public boolean equals(autorisation that) {
    if (that == null)
      return false;
    if (this == that)
      return true;

    boolean this_present_write = true;
    boolean that_present_write = true;
    if (this_present_write || that_present_write) {
      if (!(this_present_write && that_present_write))
        return false;
      if (this.write != that.write)
        return false;
    }

    boolean this_present_enabled = true;
    boolean that_present_enabled = true;
    if (this_present_enabled || that_present_enabled) {
      if (!(this_present_enabled && that_present_enabled))
        return false;
      if (this.enabled != that.enabled)
        return false;
    }

    boolean this_present_module_config = true && this.isSetModule_config();
    boolean that_present_module_config = true && that.isSetModule_config();
    if (this_present_module_config || that_present_module_config) {
      if (!(this_present_module_config && that_present_module_config))
        return false;
      if (!this.module_config.equals(that.module_config))
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    int hashCode = 1;

    hashCode = hashCode * 8191 + ((write) ? 131071 : 524287);

    hashCode = hashCode * 8191 + ((enabled) ? 131071 : 524287);

    hashCode = hashCode * 8191 + ((isSetModule_config()) ? 131071 : 524287);
    if (isSetModule_config())
      hashCode = hashCode * 8191 + module_config.hashCode();

    return hashCode;
  }

  @Override
  public int compareTo(autorisation other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;

    lastComparison = java.lang.Boolean.valueOf(isSetWrite()).compareTo(other.isSetWrite());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetWrite()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.write, other.write);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetEnabled()).compareTo(other.isSetEnabled());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetEnabled()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.enabled, other.enabled);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetModule_config()).compareTo(other.isSetModule_config());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetModule_config()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.module_config, other.module_config);
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
    java.lang.StringBuilder sb = new java.lang.StringBuilder("autorisation(");
    boolean first = true;

    sb.append("write:");
    sb.append(this.write);
    first = false;
    if (!first) sb.append(", ");
    sb.append("enabled:");
    sb.append(this.enabled);
    first = false;
    if (isSetModule_config()) {
      if (!first) sb.append(", ");
      sb.append("module_config:");
      if (this.module_config == null) {
        sb.append("null");
      } else {
        org.apache.thrift.TBaseHelper.toString(this.module_config, sb);
      }
      first = false;
    }
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
    // alas, we cannot check 'write' because it's a primitive and you chose the non-beans generator.
    // alas, we cannot check 'enabled' because it's a primitive and you chose the non-beans generator.
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
      // it doesn't seem like you should have to do this, but java serialization is wacky, and doesn't call the default constructor.
      __isset_bitfield = 0;
      read(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(in)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private static class autorisationStandardSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public autorisationStandardScheme getScheme() {
      return new autorisationStandardScheme();
    }
  }

  private static class autorisationStandardScheme extends org.apache.thrift.scheme.StandardScheme<autorisation> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, autorisation struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // WRITE
            if (schemeField.type == org.apache.thrift.protocol.TType.BOOL) {
              struct.write = iprot.readBool();
              struct.setWriteIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // ENABLED
            if (schemeField.type == org.apache.thrift.protocol.TType.BOOL) {
              struct.enabled = iprot.readBool();
              struct.setEnabledIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 3: // MODULE_CONFIG
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.module_config = iprot.readBinary();
              struct.setModule_configIsSet(true);
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
      if (!struct.isSetWrite()) {
        throw new org.apache.thrift.protocol.TProtocolException("Required field 'write' was not found in serialized data! Struct: " + toString());
      }
      if (!struct.isSetEnabled()) {
        throw new org.apache.thrift.protocol.TProtocolException("Required field 'enabled' was not found in serialized data! Struct: " + toString());
      }
      struct.validate();
    }

    public void write(org.apache.thrift.protocol.TProtocol oprot, autorisation struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      oprot.writeFieldBegin(WRITE_FIELD_DESC);
      oprot.writeBool(struct.write);
      oprot.writeFieldEnd();
      oprot.writeFieldBegin(ENABLED_FIELD_DESC);
      oprot.writeBool(struct.enabled);
      oprot.writeFieldEnd();
      if (struct.module_config != null) {
        if (struct.isSetModule_config()) {
          oprot.writeFieldBegin(MODULE_CONFIG_FIELD_DESC);
          oprot.writeBinary(struct.module_config);
          oprot.writeFieldEnd();
        }
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class autorisationTupleSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public autorisationTupleScheme getScheme() {
      return new autorisationTupleScheme();
    }
  }

  private static class autorisationTupleScheme extends org.apache.thrift.scheme.TupleScheme<autorisation> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, autorisation struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol oprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      oprot.writeBool(struct.write);
      oprot.writeBool(struct.enabled);
      java.util.BitSet optionals = new java.util.BitSet();
      if (struct.isSetModule_config()) {
        optionals.set(0);
      }
      oprot.writeBitSet(optionals, 1);
      if (struct.isSetModule_config()) {
        oprot.writeBinary(struct.module_config);
      }
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, autorisation struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol iprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      struct.write = iprot.readBool();
      struct.setWriteIsSet(true);
      struct.enabled = iprot.readBool();
      struct.setEnabledIsSet(true);
      java.util.BitSet incoming = iprot.readBitSet(1);
      if (incoming.get(0)) {
        struct.module_config = iprot.readBinary();
        struct.setModule_configIsSet(true);
      }
    }
  }

  private static <S extends org.apache.thrift.scheme.IScheme> S scheme(org.apache.thrift.protocol.TProtocol proto) {
    return (org.apache.thrift.scheme.StandardScheme.class.equals(proto.getScheme()) ? STANDARD_SCHEME_FACTORY : TUPLE_SCHEME_FACTORY).getScheme();
  }
}


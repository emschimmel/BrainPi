/**
 * Autogenerated by Thrift Compiler (0.10.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package nl.earpi.generated.earpi;

@SuppressWarnings({"cast", "rawtypes", "serial", "unchecked", "unused"})
@javax.annotation.Generated(value = "Autogenerated by Thrift Compiler (0.10.0)", date = "2018-01-01")
public class DeviceTokenItem implements org.apache.thrift.TBase<DeviceTokenItem, DeviceTokenItem._Fields>, java.io.Serializable, Cloneable, Comparable<DeviceTokenItem> {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("DeviceTokenItem");

  private static final org.apache.thrift.protocol.TField DEVICE_FIELD_DESC = new org.apache.thrift.protocol.TField("device", org.apache.thrift.protocol.TType.STRUCT, (short)1);
  private static final org.apache.thrift.protocol.TField ACTIVE_FIELD_DESC = new org.apache.thrift.protocol.TField("active", org.apache.thrift.protocol.TType.BOOL, (short)2);

  private static final org.apache.thrift.scheme.SchemeFactory STANDARD_SCHEME_FACTORY = new DeviceTokenItemStandardSchemeFactory();
  private static final org.apache.thrift.scheme.SchemeFactory TUPLE_SCHEME_FACTORY = new DeviceTokenItemTupleSchemeFactory();

  public nl.earpi.generated.autorisationstruct.DeviceTokenInput device; // required
  public boolean active; // required

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    DEVICE((short)1, "device"),
    ACTIVE((short)2, "active");

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
        case 1: // DEVICE
          return DEVICE;
        case 2: // ACTIVE
          return ACTIVE;
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
  private static final int __ACTIVE_ISSET_ID = 0;
  private byte __isset_bitfield = 0;
  public static final java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new java.util.EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.DEVICE, new org.apache.thrift.meta_data.FieldMetaData("device", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.StructMetaData(org.apache.thrift.protocol.TType.STRUCT, nl.earpi.generated.autorisationstruct.DeviceTokenInput.class)));
    tmpMap.put(_Fields.ACTIVE, new org.apache.thrift.meta_data.FieldMetaData("active", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.BOOL)));
    metaDataMap = java.util.Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(DeviceTokenItem.class, metaDataMap);
  }

  public DeviceTokenItem() {
  }

  public DeviceTokenItem(
    nl.earpi.generated.autorisationstruct.DeviceTokenInput device,
    boolean active)
  {
    this();
    this.device = device;
    this.active = active;
    setActiveIsSet(true);
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public DeviceTokenItem(DeviceTokenItem other) {
    __isset_bitfield = other.__isset_bitfield;
    if (other.isSetDevice()) {
      this.device = new nl.earpi.generated.autorisationstruct.DeviceTokenInput(other.device);
    }
    this.active = other.active;
  }

  public DeviceTokenItem deepCopy() {
    return new DeviceTokenItem(this);
  }

  @Override
  public void clear() {
    this.device = null;
    setActiveIsSet(false);
    this.active = false;
  }

  public nl.earpi.generated.autorisationstruct.DeviceTokenInput getDevice() {
    return this.device;
  }

  public DeviceTokenItem setDevice(nl.earpi.generated.autorisationstruct.DeviceTokenInput device) {
    this.device = device;
    return this;
  }

  public void unsetDevice() {
    this.device = null;
  }

  /** Returns true if field device is set (has been assigned a value) and false otherwise */
  public boolean isSetDevice() {
    return this.device != null;
  }

  public void setDeviceIsSet(boolean value) {
    if (!value) {
      this.device = null;
    }
  }

  public boolean isActive() {
    return this.active;
  }

  public DeviceTokenItem setActive(boolean active) {
    this.active = active;
    setActiveIsSet(true);
    return this;
  }

  public void unsetActive() {
    __isset_bitfield = org.apache.thrift.EncodingUtils.clearBit(__isset_bitfield, __ACTIVE_ISSET_ID);
  }

  /** Returns true if field active is set (has been assigned a value) and false otherwise */
  public boolean isSetActive() {
    return org.apache.thrift.EncodingUtils.testBit(__isset_bitfield, __ACTIVE_ISSET_ID);
  }

  public void setActiveIsSet(boolean value) {
    __isset_bitfield = org.apache.thrift.EncodingUtils.setBit(__isset_bitfield, __ACTIVE_ISSET_ID, value);
  }

  public void setFieldValue(_Fields field, java.lang.Object value) {
    switch (field) {
    case DEVICE:
      if (value == null) {
        unsetDevice();
      } else {
        setDevice((nl.earpi.generated.autorisationstruct.DeviceTokenInput)value);
      }
      break;

    case ACTIVE:
      if (value == null) {
        unsetActive();
      } else {
        setActive((java.lang.Boolean)value);
      }
      break;

    }
  }

  public java.lang.Object getFieldValue(_Fields field) {
    switch (field) {
    case DEVICE:
      return getDevice();

    case ACTIVE:
      return isActive();

    }
    throw new java.lang.IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new java.lang.IllegalArgumentException();
    }

    switch (field) {
    case DEVICE:
      return isSetDevice();
    case ACTIVE:
      return isSetActive();
    }
    throw new java.lang.IllegalStateException();
  }

  @Override
  public boolean equals(java.lang.Object that) {
    if (that == null)
      return false;
    if (that instanceof DeviceTokenItem)
      return this.equals((DeviceTokenItem)that);
    return false;
  }

  public boolean equals(DeviceTokenItem that) {
    if (that == null)
      return false;
    if (this == that)
      return true;

    boolean this_present_device = true && this.isSetDevice();
    boolean that_present_device = true && that.isSetDevice();
    if (this_present_device || that_present_device) {
      if (!(this_present_device && that_present_device))
        return false;
      if (!this.device.equals(that.device))
        return false;
    }

    boolean this_present_active = true;
    boolean that_present_active = true;
    if (this_present_active || that_present_active) {
      if (!(this_present_active && that_present_active))
        return false;
      if (this.active != that.active)
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    int hashCode = 1;

    hashCode = hashCode * 8191 + ((isSetDevice()) ? 131071 : 524287);
    if (isSetDevice())
      hashCode = hashCode * 8191 + device.hashCode();

    hashCode = hashCode * 8191 + ((active) ? 131071 : 524287);

    return hashCode;
  }

  @Override
  public int compareTo(DeviceTokenItem other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;

    lastComparison = java.lang.Boolean.valueOf(isSetDevice()).compareTo(other.isSetDevice());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetDevice()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.device, other.device);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetActive()).compareTo(other.isSetActive());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetActive()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.active, other.active);
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
    java.lang.StringBuilder sb = new java.lang.StringBuilder("DeviceTokenItem(");
    boolean first = true;

    sb.append("device:");
    if (this.device == null) {
      sb.append("null");
    } else {
      sb.append(this.device);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("active:");
    sb.append(this.active);
    first = false;
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
    if (device == null) {
      throw new org.apache.thrift.protocol.TProtocolException("Required field 'device' was not present! Struct: " + toString());
    }
    // alas, we cannot check 'active' because it's a primitive and you chose the non-beans generator.
    // check for sub-struct validity
    if (device != null) {
      device.validate();
    }
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

  private static class DeviceTokenItemStandardSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public DeviceTokenItemStandardScheme getScheme() {
      return new DeviceTokenItemStandardScheme();
    }
  }

  private static class DeviceTokenItemStandardScheme extends org.apache.thrift.scheme.StandardScheme<DeviceTokenItem> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, DeviceTokenItem struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // DEVICE
            if (schemeField.type == org.apache.thrift.protocol.TType.STRUCT) {
              struct.device = new nl.earpi.generated.autorisationstruct.DeviceTokenInput();
              struct.device.read(iprot);
              struct.setDeviceIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // ACTIVE
            if (schemeField.type == org.apache.thrift.protocol.TType.BOOL) {
              struct.active = iprot.readBool();
              struct.setActiveIsSet(true);
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
      if (!struct.isSetActive()) {
        throw new org.apache.thrift.protocol.TProtocolException("Required field 'active' was not found in serialized data! Struct: " + toString());
      }
      struct.validate();
    }

    public void write(org.apache.thrift.protocol.TProtocol oprot, DeviceTokenItem struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      if (struct.device != null) {
        oprot.writeFieldBegin(DEVICE_FIELD_DESC);
        struct.device.write(oprot);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldBegin(ACTIVE_FIELD_DESC);
      oprot.writeBool(struct.active);
      oprot.writeFieldEnd();
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class DeviceTokenItemTupleSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public DeviceTokenItemTupleScheme getScheme() {
      return new DeviceTokenItemTupleScheme();
    }
  }

  private static class DeviceTokenItemTupleScheme extends org.apache.thrift.scheme.TupleScheme<DeviceTokenItem> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, DeviceTokenItem struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol oprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      struct.device.write(oprot);
      oprot.writeBool(struct.active);
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, DeviceTokenItem struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol iprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      struct.device = new nl.earpi.generated.autorisationstruct.DeviceTokenInput();
      struct.device.read(iprot);
      struct.setDeviceIsSet(true);
      struct.active = iprot.readBool();
      struct.setActiveIsSet(true);
    }
  }

  private static <S extends org.apache.thrift.scheme.IScheme> S scheme(org.apache.thrift.protocol.TProtocol proto) {
    return (org.apache.thrift.scheme.StandardScheme.class.equals(proto.getScheme()) ? STANDARD_SCHEME_FACTORY : TUPLE_SCHEME_FACTORY).getScheme();
  }
}

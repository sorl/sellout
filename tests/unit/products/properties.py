import flexmock

from django.test import TestCase


from sellout.products import Prototype, Property


class TestPrototype(TestCase):

    def test_properties_all(self):
        p1 = Property(id=1, name='Neck')
        p2 = Property(id=2, name='Body')

        flexmock(Property.objects).should_receive('filter').with_args([]).and_return([p1, p2])
        prototype = Prototype(name='Guitars')
        prototype.property_data['items'] = [p1.id, p2.id]
        items = prototype.properties.all()

        self.assertTrue(p1 in items)
        self.assertTrue(p2 in items)

    def test_properties_set(self):
        p1 = Property(id=1, name='Neck')
        p2 = Property(id=2, name='Body')

        flexmock(Property.objects).should_receive('filter').with_args([p1.id, p2.id]).and_return([p1, p2])

        prototype = Prototype(name='Guitars')
        prototype.properties = [p1, p2]

        items = prototype.properties.all()
        self.assertTrue(p1 in items)
        self.assertTrue(p2 in items)

    def test_properties_add(self):
        p1 = Property(id=1, name='Neck')
        flexmock(Property.objects).should_receive('filter').with_args([p1.id]).and_return([p1])

        prototype = Prototype(name='Guitars')
        prototype.add(p1)
        items = prototype.properties.all()
        self.assertTrue(p1 in items)

    def test_properties_add_twice(self):
        p1 = Property(id=1, name='Neck')
        flexmock(Property.objects).should_receive('filter').with_args([p1.id]).and_return([p1])

        prototype = Prototype(name='Guitars')
        prototype.add(p1)
        prototype.add(p1)
        items = prototype.properties.all()
        self.assertTrue(p1 in items)
        self.assertTrue(len(items) == 1)

    def test_properties_remove(self):

        p1 = Property(id=1, name='Neck')
        p2 = Property(id=2, name='Body')
        flexmock(Property.objects).should_receive('filter').with_args([p1.id]).and_return([p1])

        prototype = Prototype(name='Guitars')
        prototype.property_data['items'] = [p1.id, p2.id]
        prototype.remove(p2)

        items = prototype.properties.all()
        self.assertTrue(p1 in items)
        self.assertTrue(len(items) == 1)

    def test_properties_remove_twice(self):

        p1 = Property(id=1, name='Neck')
        p2 = Property(id=2, name='Body')
        flexmock(Property.objects).should_receive('filter').with_args([p1.id]).and_return([p1])

        prototype = Prototype(name='Guitars')
        prototype.property_data['items'] = [p1.id, p2.id]
        prototype.remove(p2)
        prototype.remove(p2)

        items = prototype.properties.all()
        self.assertTrue(p1 in items)
        self.assertTrue(len(items) == 1)



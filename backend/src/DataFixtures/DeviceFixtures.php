<?php

namespace App\DataFixtures;

use App\Entity\Device;
use App\Entity\User;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Common\DataFixtures\DependentFixtureInterface;
use Doctrine\Persistence\ObjectManager;

class DeviceFixtures extends Fixture implements DependentFixtureInterface
{
    public function load(ObjectManager $manager): void
    {
        $user = new Device();
        $user
            ->setMac('04:42:1a:eb:b7:d3')
            ->setIpAddress('82.169.95.30')
            ->setUser(
                $this->getReference("user1", User::class)
            )
        ;

        $manager->persist($user);
        $manager->flush();
    }

    public function getDependencies(): array
    {
        return [UserFixtures::class];
    }
}